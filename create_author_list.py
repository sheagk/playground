#!/usr/bin/env python3

from copy import copy

### set author list here:
author_list = [
r'Shea Garrison-Kimmel',
r'Andrew Wetzel',
r'Philip F. Hopkins',
r'Robyn Sanderson',
r'Kareem El-Badry',
r'James S. Bullock',
r'Andrew Graus',
r'T.K. Chan',
r'Robert Feldmann',
r'Michael Boylan-Kolchin',
r'Christopher Hayward',
r'Alex Fitts',
r'Coral Wheeler',
r'Jenna Samuel',
r'Du{\v s}an Kere{\v s}',
r'Claude-Andr{\'e} Faucher-Gigu{\`e}re',
r'Eliot Quataert',
]



#any additional \thanks{} go here, spearated by commas (e.g. your email address for being the lead author):
thanks = {
    'Shea Garrison-Kimmel':r'$\!$sheagk@caltech.edu, Einstein Fellow',
    'Andrew Wetzel':'Caltech-Carnegie Fellow',
}


# add any orcid IDs here -- will need to have file named orcid.png in your directory (or change path below):
orcids = {
    'Shea Garrison-Kimmel':'0000-0002-4655-8128',
    'Robert Feldmann':'0000-0002-1109-1919',
}

# add affiliations here, again separated by commas
affiliations = {
    'Shea Garrison-Kimmel':'Caltech',
    'Andrew Wetzel': 'UC Davis, Caltech, Carnegie',
    'Philip F. Hopkins':'Caltech',
    'Robyn Sanderson':'Caltech, UPenn, CCA',
    'Kareem El-Badry':'UC Berkeley',
    'James S. Bullock':'UC Irvine',
    'Andrew Graus':'UC Irvine, UT Austin',
    'T.K. Chan':'UC San Diego',
    'Robert Feldmann':'Zurich',
    'Michael Boylan-Kolchin':'UT Austin',
    'Christopher Hayward':'CCA',
    'Alex Fitts':'UT Austin',
    'Coral Wheeler':'Caltech',
    'Jenna Samuel':'UC Davis',
    r'Du{\v s}an Kere{\v s}':'UC San Diego',
    r'Claude-Andr{\'e} Faucher-Gigu{\`e}re':'Northwestern',
    'Eliot Quataert':'UC Berkeley',
}


# institute addresses go here
institutions = {
    'Caltech':'TAPIR, Mailcode 350-17, California Institute of Technology, Pasadena, CA 91125, USA',
    'UC Davis':'Department of Physics, University of California, Davis, CA 95616, USA',
    'Carnegie':'The Observatories of the Carnegie Institution for Science, Pasadena, CA 91101, USA',
    'UPenn':r'Department of Physics \& Astronomy, University of Pennsylvania, 209 South 33rd St., Philadelphia, PA 19104 USA',
    'CCA':r'Center for Computational Astrophysics, Flatiron Institute, 162 5th Ave., New York, NY 10010 USA',
    'UC Berkeley':r'Department of Astronomy and Theoretical Astrophysics Center, University of California Berkeley, Berkeley, CA 94720',
    'UC Irvine':r'Center for Cosmology, Department of Physics and Astronomy, University of California, Irvine, CA 92697, USA',
    'UT Austin':r'Department of Astronomy, The University of Texas at Austin, 2515 Speedway, Stop C1400, Austin, TX 78712, USA',
    'UC San Diego':r'Department of Physics, Center for Astrophysics and Space Science, University of California at San Diego, 9500 Gilman Drive, La Jolla, CA 92093',
    'Zurich':r'Institute for Computational Science, University of Zurich, CH-8057 Zurich, Switzerland',
    'Northwestern':r'Department of Physics and Astronomy and CIERA, Northwestern University, 2145 Sheridan Road, Evanston, IL 60208, USA',
}


idx = 1
author_string = ''
used_affils = {}
for author in author_list:
    my_author_string = copy(author)
    if author in orcids:
        my_author_string += r'\textsuperscript{\href{https://orcid.org/'+orcids[author]+r'}{\includegraphics[width=2.5mm]{orcid.png}}\,}'

    if author in thanks:
        my_thanks = thanks[author].split(',')
        for th in my_thanks:
            my_author_string += r'\thanks{'+th+'}'

    my_author_string += r'\altaffilmark{'
    my_affils_numbers = []
    my_affils = affiliations[author].split(',')
    for affil in my_affils:
        affil = affil.strip()
        if affil not in used_affils:
            used_affils[affil] = idx
            idx += 1
        my_affils_numbers.append(used_affils[affil])
    my_affils_numbers.sort()
    my_author_string += ','.join([str(n) for n in my_affils_numbers])
    my_author_string += '}, \n' 
    author_string += my_author_string

affil_string = ''
affil_order = {value: key for key, value in used_affils.items()}

for idx in affil_order:
    affil = affil_order[idx]
    affil_string += r'\altaffiltext{'+str(idx)+'}{'+institutions[affil]+r'} \\'+'\n'

print("Author list:")
print(author_string)
print('\n\n')
print("Affiliations:")
print(affil_string)



















