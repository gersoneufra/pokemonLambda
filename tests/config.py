import vcr

my_vcr = vcr.VCR(path_transformer=vcr.VCR.ensure_suffix('.json'), cassette_library_dir='tests/cassettes')
