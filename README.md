# Similarity search in the ZINC database

Given a molecule, this model looks for its 100 nearest neighbors, according to ECFP4 Tanimoto similarity, in the ZINC database. Due to size constraints, the model redirects queries to the ZINC server, so when using this model predictions are posted online.

## Identifiers

* EOS model ID: `eos54c7`
* Slug: `zinc-similarity`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Similarity`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `List`
* Interpretation: List of 100 nearest neighbors

## References

* [Publication](https://www.frontiersin.org/articles/10.3389/fchem.2020.00046/full)
* [Source Code](http://130.92.106.217:8080/MCSS/)
* Ersilia contributor: [Amna-28](https://github.com/Amna-28)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos54c7)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos54c7.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos54c7) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://www.frontiersin.org/articles/10.3389/fchem.2020.00046/full) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!