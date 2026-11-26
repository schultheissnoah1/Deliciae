# Deliciae

This repository contains the source for the Deliciae website. Jekyll renders the Markdown in `site/` into static HTML. The published site uses HTML and CSS and serves image assets directly.

## Work on the site locally

Install Ruby 4.0, Bundler, and Python 3. From the repository root, run:

```sh
bundle install
bundle exec jekyll serve --source site --destination _site
```

Open http://localhost:4000 to preview the site. Edit the Markdown files for page content, `site/_layouts/default.html` for shared navigation and structure, and `site/assets/site.css` for styling.

To validate the build with the same base path used on GitHub Pages, stop the local preview and run:

```sh
JEKYLL_ENV=production bundle exec jekyll build --source site --destination _site --baseurl /Deliciae
python3 scripts/check-site.py /Deliciae
```

## Publishing

Pull requests targeting `main` build the site and check internal links and assets. Pushes to `main` also upload the validated output and deploy it to GitHub Pages. A maintainer must select **GitHub Actions** under **Settings → Pages → Build and deployment** before the first deployment. The workflow's deployment job reports the published URL.

## Project status

The scaffold includes Home, Services, and Our Work. The Figma export, approved service descriptions and imagery, contact details, and the language decision are pending. See [issue #10](https://github.com/schultheissnoah1/Deliciae/issues/10).

## Pull request previews

After the Pages workflow completes, open
`https://schultheissnoah1.github.io/Deliciae/previews/pr-<number>/` for a pull
request targeting `main` from a branch in this repository. These previews are
public. The workflow refreshes them when an eligible pull request opens,
changes, reopens, or closes. Closing a pull request removes its preview from the
next successful deployment. Fork pull requests still run build checks.
