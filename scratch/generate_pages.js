const fs = require('fs');
const path = require('path');

// Define the cities and their configuration
const citiesInfo = {
    "ambala": {
        name: "Ambala",
        travel_time: "2.5 hours",
        route: "via NH-44",
        surrounding: "Yamunanagar, Kurukshetra",
        keywords: "brain hemorrhage treatment Ambala, neurosurgeon Ambala, brain surgery Ambala, stroke treatment Ambala, Dr. Vikas Gupta, brain hemorrhage Delhi"
    },
    "bhiwani": {
        name: "Bhiwani",
        travel_time: "2 hours",
        route: "via Rohtak-Bhiwani Road",
        surrounding: "Charkhi Dadri, Rohtak",
        keywords: "brain hemorrhage treatment Bhiwani, neurosurgeon Bhiwani, brain surgery Bhiwani, stroke treatment Bhiwani, Dr. Vikas Gupta"
    },
    "charkhi-dadri": {
        name: "Charkhi Dadri",
        travel_time: "2.5 hours",
        route: "via Rohtak-Jhajjar Road",
        surrounding: "Bhiwani, Jhajjar",
        keywords: "brain hemorrhage treatment Charkhi Dadri, neurosurgeon Charkhi Dadri, brain surgery Charkhi Dadri, stroke treatment Charkhi Dadri, Dr. Vikas Gupta"
    },
    "faridabad": {
        name: "Faridabad",
        travel_time: "30 mins",
        route: "via Mathura Road",
        surrounding: "Gurgaon, Noida",
        keywords: "brain hemorrhage treatment Faridabad, neurosurgeon Faridabad, brain surgery Faridabad, stroke treatment Faridabad, Dr. Vikas Gupta"
    },
    "fatehabad": {
        name: "Fatehabad",
        travel_time: "3 hours",
        route: "via NH-9",
        surrounding: "Sirsa, Hisar",
        keywords: "brain hemorrhage treatment Fatehabad, neurosurgeon Fatehabad, brain surgery Fatehabad, stroke treatment Fatehabad, Dr. Vikas Gupta"
    },
    "gurugram": {
        name: "Gurugram",
        travel_time: "45 mins",
        route: "via NH-48",
        surrounding: "Cyber City, DLF Phase 1-5, Sohna Road",
        keywords: "brain hemorrhage treatment Gurugram, neurosurgeon Gurugram, brain surgery Gurugram, stroke treatment Gurugram, Dr. Vikas Gupta"
    },
    "hisar": {
        name: "Hisar",
        travel_time: "2.5 hours",
        route: "via NH-9",
        surrounding: "Fatehabad, Hansi",
        keywords: "brain hemorrhage treatment Hisar, neurosurgeon Hisar, brain surgery Hisar, stroke treatment Hisar, Dr. Vikas Gupta"
    },
    "jhajjar": {
        name: "Jhajjar",
        travel_time: "1.5 hours",
        route: "via NH-9 / Jhajjar Road",
        surrounding: "Bahadurgarh, Rohtak",
        keywords: "brain hemorrhage treatment Jhajjar, neurosurgeon Jhajjar, brain surgery Jhajjar, stroke treatment Jhajjar, Dr. Vikas Gupta"
    },
    "jind": {
        name: "Jind",
        travel_time: "2.5 hours",
        route: "via NH-352",
        surrounding: "Kaithal, Rohtak",
        keywords: "brain hemorrhage treatment Jind, neurosurgeon Jind, brain surgery Jind, stroke treatment Jind, Dr. Vikas Gupta"
    },
    "kaithal": {
        name: "Kaithal",
        travel_time: "3 hours",
        route: "via NH-44 and NH-152",
        surrounding: "Kurukshetra, Jind",
        keywords: "brain hemorrhage treatment Kaithal, neurosurgeon Kaithal, brain surgery Kaithal, stroke treatment Kaithal, Dr. Vikas Gupta"
    },
    "karnal": {
        name: "Karnal",
        travel_time: "2 hours",
        route: "via NH-44",
        surrounding: "Panipat, Kurukshetra",
        keywords: "brain hemorrhage treatment Karnal, neurosurgeon Karnal, brain surgery Karnal, stroke treatment Karnal, Dr. Vikas Gupta"
    },
    "kurukshetra": {
        name: "Kurukshetra",
        travel_time: "2.5 hours",
        route: "via NH-44",
        surrounding: "Ambala, Karnal",
        keywords: "brain hemorrhage treatment Kurukshetra, neurosurgeon Kurukshetra, brain surgery Kurukshetra, stroke treatment Kurukshetra, Dr. Vikas Gupta"
    },
    "mahendragarh": {
        name: "Mahendragarh",
        travel_time: "2.5 hours",
        route: "via NH-48 and NH-148B",
        surrounding: "Narnaul, Rewari",
        keywords: "brain hemorrhage treatment Mahendragarh, neurosurgeon Mahendragarh, brain surgery Mahendragarh, stroke treatment Mahendragarh, Dr. Vikas Gupta"
    },
    "nuh": {
        name: "Nuh",
        travel_time: "2 hours",
        route: "via Gurgaon-Alwar Highway",
        surrounding: "Palwal, Sohna",
        keywords: "brain hemorrhage treatment Nuh, neurosurgeon Nuh, brain surgery Nuh, stroke treatment Nuh, Dr. Vikas Gupta"
    },
    "palwal": {
        name: "Palwal",
        travel_time: "1.5 hours",
        route: "via NH-19",
        surrounding: "Faridabad, Nuh",
        keywords: "brain hemorrhage treatment Palwal, neurosurgeon Palwal, brain surgery Palwal, stroke treatment Palwal, Dr. Vikas Gupta"
    },
    "panchkula": {
        name: "Panchkula",
        travel_time: "4 hours",
        route: "via NH-44",
        surrounding: "Chandigarh, Ambala",
        keywords: "brain hemorrhage treatment Panchkula, neurosurgeon Panchkula, brain surgery Panchkula, stroke treatment Panchkula, Dr. Vikas Gupta"
    }
};

// External cities in Haryana to link in the "Other Cities" section
const externalCities = {
    "panipat": "Panipat",
    "rohtak": "Rohtak",
    "sonipat": "Sonipat"
};

function generateOtherCitiesLinks(currentCitySlug) {
    const links = [];
    
    // Add sibling brain hemorrhage pages
    const sortedBH = Object.entries(citiesInfo).sort((a, b) => a[1].name.localeCompare(b[1].name));
    for (const [slug, info] of sortedBH) {
        if (slug === currentCitySlug) continue;
        links.push(`<a href="${slug}.html" style="padding: 12px 20px; background: var(--white); border: 1px solid var(--border); border-radius: 50px; text-decoration: none; color: var(--text);">${info.name}</a>`);
    }
    
    // Add external general neurosurgeon pages
    const sortedExt = Object.entries(externalCities).sort((a, b) => a[1].localeCompare(b[1]));
    for (const [slug, name] of sortedExt) {
        links.push(`<a href="../../../../neurosurgeon/${slug}.html" style="padding: 12px 20px; background: var(--white); border: 1px solid var(--border); border-radius: 50px; text-decoration: none; color: var(--text);">${name}</a>`);
    }
    
    // Add "All Haryana Cities" link
    links.push('<a href="../../../../neurosurgeon/haryana.html" style="padding: 12px 20px; background: var(--accent); border: 1px solid var(--accent); border-radius: 50px; text-decoration: none; color: white;">All Haryana Cities</a>');
    
    return links.join('');
}

function main() {
    const haryanaDir = path.join(__dirname, "..", "conditions", "brain-hemorrhage", "india", "haryana");
    const ambalaPath = path.join(haryanaDir, "ambala.html");
    
    // Read the master template (which currently is ambala.html)
    let masterContent = fs.readFileSync(ambalaPath, "utf-8");
    
    // Standardize links to root resources in the master template (idempotent regex replacement)
    masterContent = masterContent.replace(/(\.\.\/){3,5}style\.css/g, "../../../../style.css");
    masterContent = masterContent.replace(/(\.\.\/){3,5}index\.html/g, "../../../../index.html");
    masterContent = masterContent.replace(/(\.\.\/){3,5}assets\/logo\.jpg/g, "../../../../assets/logo.jpg");
    masterContent = masterContent.replace(/(\.\.\/){3,5}assets\/logo\.png/g, "../../../../assets/logo.png");
    masterContent = masterContent.replace(/(\.\.\/){3,5}about-doctor\.html/g, "../../../../about-doctor.html");
    masterContent = masterContent.replace(/(\.\.\/){3,5}conditions\/stroke\.html/g, "../../../../conditions/stroke.html");
    masterContent = masterContent.replace(/(\.\.\/){3,5}conditions\/brain-aneurysm\.html/g, "../../../../conditions/brain-aneurysm.html");
    masterContent = masterContent.replace(/(\.\.\/){3,5}conditions\/brain-tumor\.html/g, "../../../../conditions/brain-tumor.html");
    masterContent = masterContent.replace(/(\.\.\/){3,5}script\.js/g, "../../../../script.js");
    
    // Standardize navigation pill link list to have the full set of links (including causes, FAQ)
    const oldNavCenter = '<div class="nav-links-center"><a href="#home">Home</a><a href="../../../../about-doctor.html">About Doctor</a><a href="#treatment">Treatment</a><a href="#symptoms">Symptoms</a><a href="#contact">Contact</a></div>';
    const newNavCenter = '<div class="nav-links-center"><a href="#home">Home</a><a href="../../../../about-doctor.html">About Doctor</a><a href="#treatment">Treatment</a><a href="#symptoms">Symptoms</a><a href="#causes">Causes</a><a href="#faq">FAQ</a><a href="#contact">Contact</a></div>';
    masterContent = masterContent.replaceAll(oldNavCenter, newNavCenter);
    
    // Parameterize the masterContent
    // Canonical link
    masterContent = masterContent.replaceAll(
        '<link rel="canonical" href="https://drvikasneuro.com/conditions/brain-hemorrhage/india/haryana/ambala.html">',
        '<link rel="canonical" href="https://drvikasneuro.com/conditions/brain-hemorrhage/india/haryana/{city_slug}.html">'
    );
    
    // Title
    masterContent = masterContent.replaceAll(
        '<title>Brain Hemorrhage Treatment in Ambala | Dr. Vikas Gupta - Best Neurosurgeon</title>',
        '<title>Brain Hemorrhage Treatment in {City} | Dr. Vikas Gupta - Best Neurosurgeon</title>'
    );
    
    // Meta description
    masterContent = masterContent.replaceAll(
        '<meta name="description" content="Expert brain hemorrhage treatment in Ambala. Dr. Vikas Gupta offers advanced neurosurgical care with 30+ years experience. Available at Kailash Deepak Hospital, Delhi. Serving Ambala, Yamunanagar, Kurukshetra.">',
        '<meta name="description" content="Expert brain hemorrhage treatment in {City}. Dr. Vikas Gupta offers advanced neurosurgical care with 30+ years experience. Available at Kailash Deepak Hospital, Delhi. Serving {City}, {Surrounding}.">'
    );
    
    // Keywords
    masterContent = masterContent.replaceAll(
        '<meta name="keywords" content="brain hemorrhage treatment Ambala, neurosurgeon Ambala, brain surgery Ambala, stroke treatment Ambala, Dr. Vikas Gupta, brain hemorrhage Delhi">',
        '<meta name="keywords" content="{Keywords}">'
    );
    
    // Hero badge
    masterContent = masterContent.replaceAll(
        '<span class="hero-badge">BRAIN HEMORRHAGE TREATMENT IN AMBALA</span>',
        '<span class="hero-badge">BRAIN HEMORRHAGE TREATMENT IN {CITY_UPPER}</span>'
    );
    
    // Hero Title
    masterContent = masterContent.replaceAll(
        '<h1>Expert Brain Hemorrhage <span>Treatment in Ambala</span></h1>',
        '<h1>Expert Brain Hemorrhage <span>Treatment in {City}</span></h1>'
    );
    
    // Hero Paragraph
    masterContent = masterContent.replaceAll(
        '<p>Dr. Vikas Gupta is the leading neurosurgeon providing advanced brain hemorrhage treatment to patients from Ambala, Yamunanagar, Kurukshetra, and surrounding areas. With 30+ years of experience at Kailash Deepak Hospital, Delhi.</p>',
        '<p>Dr. Vikas Gupta is the leading neurosurgeon providing advanced brain hemorrhage treatment to patients from {City}, {Surrounding}, and surrounding areas. With 30+ years of experience at Kailash Deepak Hospital, Delhi.</p>'
    )
    
    // Location indicator
    masterContent = masterContent.replaceAll(
        '<div class="location-indicator"><span class="location-badge"><span class="location-dot"></span>Available at Kailash Deepak Hospital, Delhi — 2.5 hours from Ambala</span></div>',
        '<div class="location-indicator"><span class="location-badge"><span class="location-dot"></span>Available at Kailash Deepak Hospital, Delhi — {Travel_Time} from {City}</span></div>'
    );
    
    // WhatsApp URL
    masterContent = masterContent.replaceAll(
        'https://wa.me/919810501521?text=Brain%20Hemorrhage%20Treatment%20in%20Ambala%0Ahttps%3A%2F%2Fdrvikasneuro.com%2Fconditions%2Fbrain-hemorrhage%2Findia%2Fharyana%2Fambala.html',
        '{WhatsApp_URL}'
    );
    
    // Treatment Section Header
    masterContent = masterContent.replaceAll(
        '<h2 class="section-title">Brain Hemorrhage Treatment in Ambala</h2>',
        '<h2 class="section-title">Brain Hemorrhage Treatment in {City}</h2>'
    );
    
    // Treatment Paragraph
    masterContent = masterContent.replaceAll(
        '<p style="max-width: 800px; margin: 0 auto; text-align: center; padding: 20px;">Dr. Vikas Gupta offers comprehensive brain hemorrhage treatment in Ambala. Brain hemorrhage (bleeding in or around the brain) requires immediate medical attention. Our advanced treatment options include surgical intervention, minimally invasive procedures, and comprehensive rehabilitation support. With state-of-the-art facilities at Kailash Deepak Hospital, Delhi, we provide world-class care for patients from Ambala and surrounding areas.</p>',
        '<p style="max-width: 800px; margin: 0 auto; text-align: center; padding: 20px;">Dr. Vikas Gupta offers comprehensive brain hemorrhage treatment in {City}. Brain hemorrhage (bleeding in or around the brain) requires immediate medical attention. Our advanced treatment options include surgical intervention, minimally invasive procedures, and comprehensive rehabilitation support. With state-of-the-art facilities at Kailash Deepak Hospital, Delhi, we provide world-class care for patients from {City} and surrounding areas.</p>'
    );
    
    // FAQ Header
    masterContent = masterContent.replaceAll(
        '<h2 class="section-title">Brain Hemorrhage Treatment in Ambala - FAQs</h2>',
        '<h2 class="section-title">Brain Hemorrhage Treatment in {City} - FAQs</h2>'
    );
    
    // FAQ Q1 Question and Answer
    masterContent = masterContent.replaceAll(
        '<div class="faq-item fade-in"><button class="faq-question"><span>How can I get brain hemorrhage treatment in Ambala?</span><span class="material-symbols-outlined notranslate faq-icon">expand_more</span></button><div class="faq-answer"><p>Dr. Vikas Gupta provides brain hemorrhage treatment to Ambala patients at Kailash Deepak Hospital, Delhi. Contact +91 9810501521 or use the appointment form. The hospital is approximately 2.5 hours from Ambala via NH-44.</p></div></div>',
        '<div class="faq-item fade-in"><button class="faq-question"><span>How can I get brain hemorrhage treatment in {City}?</span><span class="material-symbols-outlined notranslate faq-icon">expand_more</span></button><div class="faq-answer"><p>Dr. Vikas Gupta provides brain hemorrhage treatment to {City} patients at Kailash Deepak Hospital, Delhi. Contact +91 9810501521 or use the appointment form. The hospital is approximately {Travel_Time} from {City} {Route}.</p></div></div>'
    );
    
    // Contact Header
    masterContent = masterContent.replaceAll(
        '<h2 class="section-title">Get Brain Hemorrhage Treatment in Ambala</h2>',
        '<h2 class="section-title">Get Brain Hemorrhage Treatment in {City}</h2>'
    );
    
    // Contact Paragraph
    masterContent = masterContent.replaceAll(
        '<p class="section-desc">Dr. Vikas Gupta provides expert brain hemorrhage treatment to Ambala patients. Schedule your consultation today.</p>',
        '<p class="section-desc">Dr. Vikas Gupta provides expert brain hemorrhage treatment to {City} patients. Schedule your consultation today.</p>'
    );
    
    // Replace Other Cities navigation links
    const startAnchor = '<section class="locations-india" style="background: var(--bg);"><div class="container"><div class="section-header centered fade-in"><span class="section-tag">Other Cities</span><h2 class="section-title">Brain Hemorrhage Treatment Across Haryana</h2></div><div style="display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; margin-top: 30px;">';
    const endAnchor = '</div></div></div></section>';
    
    const startIdx = masterContent.indexOf(startAnchor);
    if (startIdx !== -1) {
        const endIdx = masterContent.indexOf(endAnchor, startIdx);
        if (endIdx !== -1) {
            const fullOldSection = masterContent.substring(startIdx, endIdx + endAnchor.length);
            const placeholderSection = startAnchor + "{Other_Cities_Links}" + endAnchor;
            masterContent = masterContent.replace(fullOldSection, placeholderSection);
            console.log("Successfully parameterized the Other Cities links section!");
        } else {
            console.error("Error: Could not find end anchor for Other Cities section");
        }
    } else {
        console.error("Error: Could not find start anchor for Other Cities section");
    }

    // Now generate each city page!
    for (const [slug, info] of Object.entries(citiesInfo)) {
        const cityName = info.name;
        const travelTime = info.travel_time;
        const route = info.route;
        const surrounding = info.surrounding;
        const keywords = info.keywords;
        
        // Build WhatsApp URL
        const rawText = `Brain Hemorrhage Treatment in ${cityName}\nhttps://drvikasneuro.com/conditions/brain-hemorrhage/india/haryana/${slug}.html`;
        const encodedText = encodeURIComponent(rawText);
        const whatsappUrl = `https://wa.me/919810501521?text=${encodedText}`;
        
        const otherCitiesLinks = generateOtherCitiesLinks(slug);
        
        // Fill the template
        let cityPage = masterContent;
        cityPage = cityPage.replaceAll("{city_slug}", slug);
        cityPage = cityPage.replaceAll("{City}", cityName);
        cityPage = cityPage.replaceAll("{CITY_UPPER}", cityName.toUpperCase());
        cityPage = cityPage.replaceAll("{Surrounding}", surrounding);
        cityPage = cityPage.replaceAll("{Travel_Time}", travelTime);
        cityPage = cityPage.replaceAll("{Route}", route);
        cityPage = cityPage.replaceAll("{Keywords}", keywords);
        cityPage = cityPage.replaceAll("{WhatsApp_URL}", whatsappUrl);
        cityPage = cityPage.replaceAll("{Other_Cities_Links}", otherCitiesLinks);
        
        // Write to destination file
        const destPath = path.join(haryanaDir, `${slug}.html`);
        fs.writeFileSync(destPath, cityPage, "utf-8");
        
        console.log(`Generated page for: ${cityName} -> ${destPath}`);
    }
}

main();
