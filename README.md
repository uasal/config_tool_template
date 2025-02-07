# config_tool_template
Example of a configuration repository that is used with a specific simulation tool (or group of tools).

The naming convention should be config_project_toolname. So a hypothetical example could be `config_hubble_acs`.

The directory structure is designed as follows:

- configuration parameters that are common to all tools in the repository belong in the common.toml file. 
- There should be one directory per tool (e.g. tool1, tool2). 
  Note that in many cases there may be only a single tool per configuration repository, which is acceptable.

- All tool configs must have an `_init.toml` file which contains the default set of parameters for that tool.
- Config files must contain both values and units. Units shall utilize the astropy format.
- Values without a unit will be marked as unitless
- The origin of the values should be in a comment (for now).
- At this time, no other filenames should start with an `_`. This functionality is reserved for future feature implementation(s).
- Any added configuration file must contain the *full set* of available parameters and not just overrides for the defaults.

Configuration files may contain key valued pairs, but also utilize groupings. Such as:

```toml
OD_optic1 = '50e-3m'
[sim_settings]  # settings for simulation tool
npix = 4096 # number of pixels per frame
beamrad = 0.4 # fractional beam radius
```


## Configuration FAQ

#. How do I find all the configuration repositories?
- Search Github repos and GitLab repositories for anything named `config_`

#. Does my tool require a separate configuration repository?
- In cases where your tool is being used to conduct analyses or is related to the determination of budgets or requirements then it is advised to have a separate configuration repository that contains the defaults which should be called

#. Why/When should config files be stored separately from the code?
- Facilitates easy versioning (and impact assessment) between code changes and config changes
- Single configs can/should be usable with different versions/branches/tags
- Multiple people (or instances) can use them without permission from the code owners
- Allows for rapid automated unit testing that verifies file is readable/parse-able so you don’t accidentally break your or someone else’s code
- Allows for configurations that are specific to a site/machine/setup

#. Where should I put the configuration for my tool?
- If your tool is often used in combination with another tool, then it may make sense to share a configuration directory, otherwise it should be separate.

#. Do ALL configuration repositories need to be packages? 
- No, but it may be useful.
- We do require for traceability in reporting, which means we need to know which tags/versions you were running, and how your simulation was configured, so what is most important is that your config repo is maintained and versioned correctly. 

- Advantages to python packages: can rely on your environment to take care of directory management
  - Allows functionality to be built into package and shared between users.
- Advantages to repos with just files: 
  - Easier to maintain, must hard code a repo (bad), or set an environment variable (less bad), then execute system commands from within a python script/notebook.
   Currently doing this in psd_utils to detect if stp_reference data is dirty.

#. Config files mention filenames, where should those files be located?
- They should reside in the `support_data` directory.
  Note that in many cases the support data will contain files managed by [gitlfs](https://git-lfs.com/).

#. Do filenames or paths in config files require a unit?
Good question! This is currently being explored. They can be left blank for now.

#. When should the configuration version be augmented?
- configuration versions are not currently tracked. 
- Normally, when the code is no longer backwards compatible and the format for the file no longer applies.
  This occurs when either additional mandatory keywords are required or removed.
  This cannot be implemented because the tools are not utilizes schemas for configuration and therefore config files cannot be validated against versions of the schemas.

#. Should I use [symantic versioning](https://semver.org/)? 
Generally not as only major revisions require version bumps.



<!-- This code uses ``pre-commit`` to check yaml file syntax, maintain ``black`` formatting, and check ``flake8`` compliance.
To enable this, run the following commands once (the first removes the previous pre-commit hook)::

    git config --unset-all core.hooksPath
    pre-commit install -->
