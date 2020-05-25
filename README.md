# Template for EPL's UCLouvain Ph.D. Theses

This repository contains a template to write your thesis with the CIACO's requirements.
Just look at thesis.tex and start writing :-)

NB: For the bibliography, use Biber instead of BibTex.

## Continuous Integration with GitHub

If you use GitHub to host your repository, you can leverage the GitHub Actions to auto-generate the thesis PDF.
For this, you have a few environment variables to configure this workflow:

| env variable  | purpose   |
|---|---|
| **MAIN_LATEX**  | The entry point of your thesis (here it is thesis.tex)  |
| **FINAL_FILENAME**   | The final name of the file, which follows the naming conventions of the UCLouvain (for example :  Yakoub_13861700_2020.pdf )   |
| **DATE_TIMEZONE**  | The timezone for release (by default, Github uses GMT timezone)  |

Then in the Actions tab of your GitHub repository, you can build the thesis.