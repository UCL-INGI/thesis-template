# Template for EPL's UCLouvain Ph.D. Theses

This repository contains a template to write your thesis with the CIACO's requirements.
Just look at either thesis_a4.tex or thesis_elec.tex and start writing :-)

NB: For the bibliography, use Biber instead of BibTex.

## Thesis format

Two main files are proposed: either writing on A4 format (thesis_a4.tex) or on the CIACO specific one (thesis_elec.tex).
Both formats should work for the CIACO, but make sure you mention the format you use when sending your PDF for printing!

## Continuous Integration with GitHub

If you use GitHub to host your repository, you can leverage the GitHub Actions to auto-generate the thesis PDF.
For this, you have a few environment variables to configure this workflow:

| env variable  | purpose   |
|---|---|
| **MAIN_LATEX**  | The entry point of your thesis (here it is thesis_elec.tex)  |
| **FINAL_FILENAME**   | The final name of the file, which follows the naming conventions of the UCLouvain (for example :  Yakoub_13861700_2020.pdf )   |
| **DATE_TIMEZONE**  | The timezone for release (by default, Github uses GMT timezone)  |

Then in the Actions tab of your GitHub repository, you can build the thesis.