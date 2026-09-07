Nama : Kevin R

NPM : 2506621466

Kelas : PBP C

#Hi from another branch

# 7/9/2026
## A.Weekly Instruction Step :
1. Clone this repository
    git clone https://github.com/ke-Vyn/myportofolio.git
    cd myportofolio
2. Create a virtual environment and activate it
    python -m venv env
    env\Scripts\activate
3. Install Dependencies 
    pip install -r requirements.txt
4. Run server
    python manage.py runserver
5. Open `http://localhost:8000` in any browser

## B. Weekly Updates :
1. Added a new Highlights section containing 3 cards: Skill, Education, Projects 
2. Added a navigation button in the social links area that scrolls to the new section via anchor link (#highlights)
3. CSS styling:
    a. 3 column grid layout (display: grid), collapses into a single column on mobile / smaller screen
    b. Hover effect on each card (lift & shadow)
    c. Short fade-in entrance animation (@keyframes) when the page loads
4. Adjusted the Hero section to fill the full viewport height (min-height: 100vh) so that Highlights stays hidden until the user scrolls
5. Replaced all sample data with my own information

## C. Reflection :
### Assignment 1
1. Yes, i used semantic HTML5 elements (<header>, <main>, <section>, <footer>) to structure the page based on its content's purpose. I separated the "About Me" content into a <section class="hero"> and the new content into <section class="Highlights">. I also used <dl>, <dt> and <dd> to display NPM and study program since they're a label value pair. This made the structure easier to read from the HTML, and should also make the page look more readable for readers.

2. The main challenge was deciding how elements should reflow when the grid changes from 2 column to 1 column (mobile). On laptop / desktop, the hero section places the photo beside the identity and details using 'grid-template-areas'. If it wasn't reordered, the photo could end up appearing last, even though it's one of more important elements. I addressed this by rearranging 'grid-template'areas' so the order becomes identity > photo > details when stacked vertically on mobile. I also set the photo's maximum width to 220px on mobile so that it wouldn't dominate smaller screen. For the highlights section, i changed the grid from 3 columns to 1 column below 700px, so each card would have enough horizontal space to read comfortably.

3. Static website forces me to write every content directly into the HTML and redeploy it whenever theres changes. This becomes limiting if i want to frequently add new contents. Not only that, it also limits the website's ability to process visitor input. For example, the current "Email" button only uses a mail:to link, which opens the visitor's email client instead of allowing the web to process the message directly. For the next iteration, i'd like to add a database so contents can easily managed through an admin panel without directly editing the index.html file.

## D. AI Disclosure : 
- Tool used: Gemini AI
- How it was used: Discussed suitable CSS styling approaches, such as: grid layout, hover effects and entrance animation, for the highlights section and hero layout, based on a web design i previously created in Figma without implementing JavaScript and relying solely on CSS3