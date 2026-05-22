import os
import urllib.parse

# Define the cities and their configuration
cities_info = {
    "ambala": {
        "name": "Ambala",
        "travel_time": "2.5 hours",
        "route": "via NH-44",
        "surrounding": "Yamunanagar, Kurukshetra",
        "keywords": "brain hemorrhage treatment Ambala, neurosurgeon Ambala, brain surgery Ambala, stroke treatment Ambala, Dr. Vikas Gupta, brain hemorrhage Delhi"
    },
    "bhiwani": {
        "name": "Bhiwani",
        "travel_time": "2 hours",
        "route": "via Rohtak-Bhiwani Road",
        "surrounding": "Charkhi Dadri, Rohtak",
        "keywords": "brain hemorrhage treatment Bhiwani, neurosurgeon Bhiwani, brain surgery Bhiwani, stroke treatment Bhiwani, Dr. Vikas Gupta"
    },
    "charkhi-dadri": {
        "name": "Charkhi Dadri",
        "travel_time": "2.5 hours",
        "route": "via Rohtak-Jhajjar Road",
        "surrounding": "Bhiwani, Jhajjar",
        "keywords": "brain hemorrhage treatment Charkhi Dadri, neurosurgeon Charkhi Dadri, brain surgery Charkhi Dadri, stroke treatment Charkhi Dadri, Dr. Vikas Gupta"
    },
    "faridabad": {
        "name": "Faridabad",
        "travel_time": "30 mins",
        "route": "via Mathura Road",
        "surrounding": "Gurgaon, Noida",
        "keywords": "brain hemorrhage treatment Faridabad, neurosurgeon Faridabad, brain surgery Faridabad, stroke treatment Faridabad, Dr. Vikas Gupta"
    },
    "fatehabad": {
        "name": "Fatehabad",
        "travel_time": "3 hours",
        "route": "via NH-9",
        "surrounding": "Sirsa, Hisar",
        "keywords": "brain hemorrhage treatment Fatehabad, neurosurgeon Fatehabad, brain surgery Fatehabad, stroke treatment Fatehabad, Dr. Vikas Gupta"
    },
    "gurugram": {
        "name": "Gurugram",
        "travel_time": "45 mins",
        "route": "via NH-48",
        "surrounding": "Cyber City, DLF Phase 1-5, Sohna Road",
        "keywords": "brain hemorrhage treatment Gurugram, neurosurgeon Gurugram, brain surgery Gurugram, stroke treatment Gurugram, Dr. Vikas Gupta"
    },
    "hisar": {
        "name": "Hisar",
        "travel_time": "2.5 hours",
        "route": "via NH-9",
        "surrounding": "Fatehabad, Hansi",
        "keywords": "brain hemorrhage treatment Hisar, neurosurgeon Hisar, brain surgery Hisar, stroke treatment Hisar, Dr. Vikas Gupta"
    },
    "jhajjar": {
        "name": "Jhajjar",
        "travel_time": "1.5 hours",
        "route": "via NH-9 / Jhajjar Road",
        "surrounding": "Bahadurgarh, Rohtak",
        "keywords": "brain hemorrhage treatment Jhajjar, neurosurgeon Jhajjar, brain surgery Jhajjar, stroke treatment Jhajjar, Dr. Vikas Gupta"
    },
    "jind": {
        "name": "Jind",
        "travel_time": "2.5 hours",
        "route": "via NH-352",
        "surrounding": "Kaithal, Rohtak",
        "keywords": "brain hemorrhage treatment Jind, neurosurgeon Jind, brain surgery Jind, stroke treatment Jind, Dr. Vikas Gupta"
    },
    "kaithal": {
        "name": "Kaithal",
        "travel_time": "3 hours",
        "route": "via NH-44 and NH-152",
        "surrounding": "Kurukshetra, Jind",
        "keywords": "brain hemorrhage treatment Kaithal, neurosurgeon Kaithal, brain surgery Kaithal, stroke treatment Kaithal, Dr. Vikas Gupta"
    },
    "karnal": {
        "name": "Karnal",
        "travel_time": "2 hours",
        "route": "via NH-44",
        "surrounding": "Panipat, Kurukshetra",
        "keywords": "brain hemorrhage treatment Karnal, neurosurgeon Karnal, brain surgery Karnal, stroke treatment Karnal, Dr. Vikas Gupta"
    },
    "kurukshetra": {
        "name": "Kurukshetra",
        "travel_time": "2.5 hours",
        "route": "via NH-44",
        "surrounding": "Ambala, Karnal",
        "keywords": "brain hemorrhage treatment Kurukshetra, neurosurgeon Kurukshetra, brain surgery Kurukshetra, stroke treatment Kurukshetra, Dr. Vikas Gupta"
    },
    "mahendragarh": {
        "name": "Mahendragarh",
        "travel_time": "2.5 hours",
        "route": "via NH-48 and NH-148B",
        "surrounding": "Narnaul, Rewari",
        "keywords": "brain hemorrhage treatment Mahendragarh, neurosurgeon Mahendragarh, brain surgery Mahendragarh, stroke treatment Mahendragarh, Dr. Vikas Gupta"
    },
    "nuh": {
        "name": "Nuh",
        "travel_time": "2 hours",
        "route": "via Gurgaon-Alwar Highway",
        "surrounding": "Palwal, Sohna",
        "keywords": "brain hemorrhage treatment Nuh, neurosurgeon Nuh, brain surgery Nuh, stroke treatment Nuh, Dr. Vikas Gupta"
    },
    "palwal": {
        "name": "Palwal",
        "travel_time": "1.5 hours",
        "route": "via NH-19",
        "surrounding": "Faridabad, Nuh",
        "keywords": "brain hemorrhage treatment Palwal, neurosurgeon Palwal, brain surgery Palwal, stroke treatment Palwal, Dr. Vikas Gupta"
    },
    "panchkula": {
        "name": "Panchkula",
        "travel_time": "4 hours",
        "route": "via NH-44",
        "surrounding": "Chandigarh, Ambala",
        "keywords": "brain hemorrhage treatment Panchkula, neurosurgeon Panchkula, brain surgery Panchkula, stroke treatment Panchkula, Dr. Vikas Gupta"
    }
}

# External cities in Haryana to link in the "Other Cities" section
external_cities = {
    "panipat": "Panipat",
    "rohtak": "Rohtak",
    "sonipat": "Sonipat"
}

def generate_other_cities_links(current_city_slug):
    links = []
    
    # Add sibling brain hemorrhage pages
    for slug, info in sorted(cities_info.items(), key=lambda x: x[1]['name']):
        if slug == current_city_slug:
            continue
        links.append(f'<a href="{slug}.html" style="padding: 12px 20px; background: var(--white); border: 1px solid var(--border); border-radius: 50px; text-decoration: none; color: var(--text);">{info["name"]}</a>')
        
    # Add external general neurosurgeon pages
    for slug, name in sorted(external_cities.items(), key=lambda x: x[1]):
        links.append(f'<a href="../../../../neurosurgeon/{slug}.html" style="padding: 12px 20px; background: var(--white); border: 1px solid var(--border); border-radius: 50px; text-decoration: none; color: var(--text);">{name}</a>')
        
    # Add "All Haryana Cities" link
    links.append('<a href="../../../../neurosurgeon/haryana.html" style="padding: 12px 20px; background: var(--accent); border: 1px solid var(--accent); border-radius: 50px; text-decoration: none; color: white;">All Haryana Cities</a>')
    
    return "".join(links)

def main():
    haryana_dir = r"c:\Users\User\Desktop\spineandbrainhealers\Vijay-Gupta\conditions\brain-hemorrhage\india\haryana"
    ambala_path = os.path.join(haryana_dir, "ambala.html")
    
    # Read the master template
    with open(ambala_path, "r", encoding="utf-8") as f:
        master_content = f.read()
        
    # Standardize links to root resources in the master template
    # Replace relative path prefix ../../../ with ../../../../ for resources
    master_content = master_content.replace("../../../style.css", "../../../../style.css")
    master_content = master_content.replace("../../../index.html", "../../../../index.html")
    master_content = master_content.replace("../../../assets/logo.jpg", "../../../../assets/logo.jpg")
    master_content = master_content.replace("../../../assets/logo.png", "../../../../assets/logo.png")
    master_content = master_content.replace("../../../about-doctor.html", "../../../../about-doctor.html")
    master_content = master_content.replace("../../../conditions/stroke.html", "../../../../conditions/stroke.html")
    master_content = master_content.replace("../../../conditions/brain-aneurysm.html", "../../../../conditions/brain-aneurysm.html")
    master_content = master_content.replace("../../../conditions/brain-tumor.html", "../../../../conditions/brain-tumor.html")
    master_content = master_content.replace("../../../script.js", "../../../../script.js")
    
    # Standardize navigation pill link list to have the full set of links
    old_nav_center = '<div class="nav-links-center"><a href="#home">Home</a><a href="../../../../about-doctor.html">About Doctor</a><a href="#treatment">Treatment</a><a href="#symptoms">Symptoms</a><a href="#contact">Contact</a></div>'
    new_nav_center = '<div class="nav-links-center"><a href="#home">Home</a><a href="../../../../about-doctor.html">About Doctor</a><a href="#treatment">Treatment</a><a href="#symptoms">Symptoms</a><a href="#causes">Causes</a><a href="#faq">FAQ</a><a href="#contact">Contact</a></div>'
    master_content = master_content.replace(old_nav_center, new_nav_center)
    
    # Let's replace ambala-specific content with placeholders
    # We will find the Ambala configurations and replace them.
    # Note: We must be careful not to corrupt the rest of the text.
    
    # Replace canonical link
    master_content = master_content.replace(
        '<link rel="canonical" href="https://drvikasneuro.com/conditions/brain-hemorrhage/india/haryana/ambala.html">',
        '<link rel="canonical" href="https://drvikasneuro.com/conditions/brain-hemorrhage/india/haryana/{city_slug}.html">'
    )
    
    # Replace title
    master_content = master_content.replace(
        '<title>Brain Hemorrhage Treatment in Ambala | Dr. Vikas Gupta - Best Neurosurgeon</title>',
        '<title>Brain Hemorrhage Treatment in {City} | Dr. Vikas Gupta - Best Neurosurgeon</title>'
    )
    
    # Replace meta description
    master_content = master_content.replace(
        '<meta name="description" content="Expert brain hemorrhage treatment in Ambala. Dr. Vikas Gupta offers advanced neurosurgical care with 30+ years experience. Available at Kailash Deepak Hospital, Delhi. Serving Ambala, Yamunanagar, Kurukshetra.">',
        '<meta name="description" content="Expert brain hemorrhage treatment in {City}. Dr. Vikas Gupta offers advanced neurosurgical care with 30+ years experience. Available at Kailash Deepak Hospital, Delhi. Serving {City}, {Surrounding}.">'
    )
    
    # Replace keywords
    master_content = master_content.replace(
        '<meta name="keywords" content="brain hemorrhage treatment Ambala, neurosurgeon Ambala, brain surgery Ambala, stroke treatment Ambala, Dr. Vikas Gupta, brain hemorrhage Delhi">',
        '<meta name="keywords" content="{Keywords}">'
    )
    
    # Replace Hero badge
    master_content = master_content.replace(
        '<span class="hero-badge">BRAIN HEMORRHAGE TREATMENT IN AMBALA</span>',
        '<span class="hero-badge">BRAIN HEMORRHAGE TREATMENT IN {CITY_UPPER}</span>'
    )
    
    # Replace Hero Title
    master_content = master_content.replace(
        '<h1>Expert Brain Hemorrhage <span>Treatment in Ambala</span></h1>',
        '<h1>Expert Brain Hemorrhage <span>Treatment in {City}</span></h1>'
    )
    
    # Replace Hero Paragraph
    master_content = master_content.replace(
        '<p>Dr. Vikas Gupta is the leading neurosurgeon providing advanced brain hemorrhage treatment to patients from Ambala, Yamunanagar, Kurukshetra, and surrounding areas. With 30+ years of experience at Kailash Deepak Hospital, Delhi.</p>',
        '<p>Dr. Vikas Gupta is the leading neurosurgeon providing advanced brain hemorrhage treatment to patients from {City}, {Surrounding}, and surrounding areas. With 30+ years of experience at Kailash Deepak Hospital, Delhi.</p>'
    )
    
    # Replace Location indicator
    master_content = master_content.replace(
        '<div class="location-indicator"><span class="location-badge"><span class="location-dot"></span>Available at Kailash Deepak Hospital, Delhi — 2.5 hours from Ambala</span></div>',
        '<div class="location-indicator"><span class="location-badge"><span class="location-dot"></span>Available at Kailash Deepak Hospital, Delhi — {Travel_Time} from {City}</span></div>'
    )
    
    # Replace WhatsApp Link
    # Note that ambala.html has:
    # <div class="hero-cta"><a href="#contact" class="btn-primary">Book Appointment</a><a href="https://wa.me/919810501521?text=Brain%20Hemorrhage%20Treatment%20in%20Ambala%0Ahttps%3A%2F%2Fdrvikasneuro.com%2Fconditions%2Fbrain-hemorrhage%2Findia%2Fharyana%2Fambala.html" target="_blank" class="btn-whatsapp">
    master_content = master_content.replace(
        'https://wa.me/919810501521?text=Brain%20Hemorrhage%20Treatment%20in%20Ambala%0Ahttps%3A%2F%2Fdrvikasneuro.com%2Fconditions%2Fbrain-hemorrhage%2Findia%2Fharyana%2Fambala.html',
        '{WhatsApp_URL}'
    )
    
    # Replace Treatment Section Header
    master_content = master_content.replace(
        '<h2 class="section-title">Brain Hemorrhage Treatment in Ambala</h2>',
        '<h2 class="section-title">Brain Hemorrhage Treatment in {City}</h2>'
    )
    
    # Replace Treatment Paragraph
    master_content = master_content.replace(
        '<p style="max-width: 800px; margin: 0 auto; text-align: center; padding: 20px;">Dr. Vikas Gupta offers comprehensive brain hemorrhage treatment in Ambala. Brain hemorrhage (bleeding in or around the brain) requires immediate medical attention. Our advanced treatment options include surgical intervention, minimally invasive procedures, and comprehensive rehabilitation support. With state-of-the-art facilities at Kailash Deepak Hospital, Delhi, we provide world-class care for patients from Ambala and surrounding areas.</p>',
        '<p style="max-width: 800px; margin: 0 auto; text-align: center; padding: 20px;">Dr. Vikas Gupta offers comprehensive brain hemorrhage treatment in {City}. Brain hemorrhage (bleeding in or around the brain) requires immediate medical attention. Our advanced treatment options include surgical intervention, minimally invasive procedures, and comprehensive rehabilitation support. With state-of-the-art facilities at Kailash Deepak Hospital, Delhi, we provide world-class care for patients from {City} and surrounding areas.</p>'
    )
    
    # Replace FAQ Header
    master_content = master_content.replace(
        '<h2 class="section-title">Brain Hemorrhage Treatment in Ambala - FAQs</h2>',
        '<h2 class="section-title">Brain Hemorrhage Treatment in {City} - FAQs</h2>'
    )
    
    # Replace FAQ Q1 Question
    master_content = master_content.replace(
        '<span>How can I get brain hemorrhage treatment in Ambala?</span>',
        '<span>How can I get brain hemorrhage treatment in {City}?</span>'
    )
    
    # Replace FAQ Q1 Answer
    master_content = master_content.replace(
        '<div class="faq-answer"><p>Dr. Vikas Gupta provides brain hemorrhage treatment to Ambala patients at Kailash Deepak Hospital, Delhi. Contact +91 9810501521 or use the appointment form. The hospital is approximately 2.5 hours from Ambala via NH-44.</p></div>',
        '<div class="faq-answer"><p>Dr. Vikas Gupta provides brain hemorrhage treatment to {City} patients at Kailash Deepak Hospital, Delhi. Contact +91 9810501521 or use the appointment form. The hospital is approximately {Travel_Time} from {City} {Route}.</p></div>'
    )
    
    # Replace Contact Header
    master_content = master_content.replace(
        '<h2 class="section-title">Get Brain Hemorrhage Treatment in Ambala</h2>',
        '<h2 class="section-title">Get Brain Hemorrhage Treatment in {City}</h2>'
    )
    
    # Replace Contact Paragraph
    master_content = master_content.replace(
        '<p class="section-desc">Dr. Vikas Gupta provides expert brain hemorrhage treatment to Ambala patients. Schedule your consultation today.</p>',
        '<p class="section-desc">Dr. Vikas Gupta provides expert brain hemorrhage treatment to {City} patients. Schedule your consultation today.</p>'
    )
    
    # Locate other cities navigation div to replace
    # We will search for the entire div and replace it with a placeholder
    start_anchor = '<section class="locations-india" style="background: var(--bg);"><div class="container"><div class="section-header centered fade-in"><span class="section-tag">Other Cities</span><h2 class="section-title">Brain Hemorrhage Treatment Across Haryana</h2></div><div style="display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; margin-top: 30px;">'
    end_anchor = '</div></div></div></section>'
    
    start_idx = master_content.find(start_anchor)
    if start_idx != -1:
        end_idx = master_content.find(end_anchor, start_idx)
        if end_idx != -1:
            full_old_section = master_content[start_idx : end_idx + len(end_anchor)]
            placeholder_section = start_anchor + "{Other_Cities_Links}" + end_anchor
            master_content = master_content.replace(full_old_section, placeholder_section)
            print("Successfully parameterized the Other Cities links section!")
        else:
            print("Error: Could not find end anchor for Other Cities section")
    else:
        print("Error: Could not find start anchor for Other Cities section")

    # Now generate each city page!
    for slug, info in cities_info.items():
        city_name = info["name"]
        travel_time = info["travel_time"]
        route = info["route"]
        surrounding = info["surrounding"]
        keywords = info["keywords"]
        
        # Build the WhatsApp url
        raw_text = f"Brain Hemorrhage Treatment in {city_name}\nhttps://drvikasneuro.com/conditions/brain-hemorrhage/india/haryana/{slug}.html"
        encoded_text = urllib.parse.quote(raw_text)
        whatsapp_url = f"https://wa.me/919810501521?text={encoded_text}"
        
        other_cities_links = generate_other_cities_links(slug)
        
        # Fill the template
        city_page = master_content.format(
            city_slug=slug,
            City=city_name,
            CITY_UPPER=city_name.upper(),
            Surrounding=surrounding,
            Travel_Time=travel_time,
            Route=route,
            Keywords=keywords,
            WhatsApp_URL=whatsapp_url,
            Other_Cities_Links=other_cities_links
        )
        
        # Write to file
        dest_path = os.path.join(haryana_dir, f"{slug}.html")
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(city_page)
            
        print(f"Generated page for: {city_name} -> {dest_path}")

if __name__ == "__main__":
    main()
