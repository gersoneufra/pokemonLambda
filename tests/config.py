import vcr

PARAMS = {
    "path_transformer": vcr.VCR.ensure_suffix('.json'),
    "cassette_library_dir": 'tests/cassettes'
}

MY_VRC = vcr.VCR(**PARAMS)
