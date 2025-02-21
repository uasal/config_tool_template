# Support Data
Files that are to be added to the `support_data` directory should be broken into sub-directories that match their data type. 

**NOTE:** Keep support data within the configuration repository that makes the most sense in terms of its content. If support data can be used at a 'higher' level for a config repository within the same project, it should located there instead.

Providing a `README.md` within this directory (this file) with an overview of what type of content is within each sub-directory (but not indexing it) is a useful addition. Rough example shown below:

## Coatings
Data in [coatings](/coatings/) contains csv files with Specular Reflectance values at different wavelengths per coating type. Name of the files should include what the coating is for reference if not provided already within the csv file.

## Archive
Use the archive directory for any support data that is no longer needed or applicable to the project the config repository is associated with but does not necessary needs to be deleted. This is allows previous support data to be still easily accessible for referencing but not be mixed in with the other 'active' support data files.

Ex.) Coating reflectance data for a previous coating material that is no longer applicable to the project but was used for support data in earlier on.