import os
import subprocess
import shutil

root = "/home/veer/Ranveer/Suraj"
assets_cond = os.path.join(root, "assets/conditions")
assets_proc = os.path.join(root, "assets/procedures")

os.makedirs(assets_cond, exist_ok=True)
os.makedirs(assets_proc, exist_ok=True)

def clean_and_convert(src_dir, dest_dir):
    print(f"Processing {src_dir}...")
    for filename in os.listdir(src_dir):
        if filename.endswith(".html"):
            continue
        
        # Identify image extension
        ext = ""
        if ".webp" in filename.lower():
            ext = ".webp"
        elif ".png" in filename.lower():
            ext = ".png"
        elif ".jpg" in filename.lower() or ".jpeg" in filename.lower():
            ext = ".jpg"
        
        if not ext:
            continue

        src_path = os.path.join(src_dir, filename)
        
        # Clean up the name. Use the base name before any extra dots/underscores
        # e.g. "stroke.jpg" -> "stroke"
        # e.g. "stroke.jpg_.webp" -> "stroke"
        base_name = filename
        for e in [".jpg", ".jpeg", ".webp", ".png", ".jpg_", ".jpeg_", ".png_"]:
            if e in base_name:
                base_name = base_name.split(e)[0]
        
        if not base_name: # Handle cases like ".webp"
            base_name = filename.split(".")[0]

        dest_path = os.path.join(dest_dir, f"{base_name}.jpg")
        
        print(f"  Converting {filename} -> {base_name}.jpg")
        
        # Convert to JPG using ImageMagick
        try:
            subprocess.run(["magick", src_path, dest_path], check=True)
            # Remove the original file from the HTML directory
            os.remove(src_path)
            
            # Check dimensions
            result = subprocess.run(["magick", "identify", "-format", "%w %h", dest_path], capture_output=True, text=True)
            w, h = map(int, result.stdout.split())
            ratio = w / h
            print(f"    Dimensions: {w}x{h} (Ratio: {ratio:.2f})")
            if ratio < 0.8 or ratio > 2.0:
                print(f"    WARNING: Unusual aspect ratio for {base_name}.jpg")
        except Exception as e:
            print(f"    Error processing {filename}: {e}")

clean_and_convert(os.path.join(root, "conditions"), assets_cond)
clean_and_convert(os.path.join(root, "procedures"), assets_proc)

print("Finished processing images.")
