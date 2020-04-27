#!/usr/bin/env python3

'''
TODO: Description Needed

'''

def test_alloy():

    from software.build.alloy import binary_alloy

    #### Traditional ASE functionality #####
    from software.examples.data.model_gen import get_example_slab as slab
    slab = slab()
    #########

    alloy_slab = binary_alloy(slab, 'Pd', 8)
    assert(alloy_slab.get_chemical_symbols().count('Pd') == 8)
    assert(alloy_slab.get_chemical_symbols().count('Au') == 10)

test_alloy()