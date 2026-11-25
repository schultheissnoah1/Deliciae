# Deliciae

Deliciae is the source repository for a static website intended for GitHub Pages. The project uses Markdown for authoring, HTML for page structure, and CSS for presentation. The planned GitHub Actions workflow will turn the source files into a website and publish the generated files to GitHub Pages.

## Content and design

Markdown files contain the text and structure of the website. Authors can use headings to organize a page, lists to group related information, and links to connect readers to other pages. A content update starts with an edit to the relevant Markdown file, which can be reviewed in Git alongside any related changes.

The build will convert Markdown into HTML that browsers can display. CSS will control the site's presentation, including typography, spacing, colors, and layout. Keeping these styles in CSS allows a design change to apply across pages while keeping the Markdown focused on the content.

## Build and publication

1. **Update the source.** Add or revise Markdown content, or update the CSS when the site's presentation needs to change.
2. **Generate the pages.** GitHub Actions will run the site build and render the Markdown as HTML. Markdown links, headings, and lists will become the corresponding HTML elements.
3. **Prepare the site files.** The build will assemble the generated HTML and its stylesheets into the directory that GitHub Pages will serve.
4. **Deploy to GitHub Pages.** The deployment will publish the static files. Visitors' browsers will load the generated HTML and apply the accompanying CSS. The published site will run without client-side JavaScript or a server-side application.

## Project status

The repository currently contains this README. The site content, stylesheets, and GitHub Actions workflow are planned. The Markdown renderer, file layout, and deployment trigger will be defined when the publishing workflow is implemented.
