# github_updater
A python module / git submodule for python applications to grab their updates from github releases

Define the updater's settings in the **parent folder.** eg if you put the module in /project/github_updater the settings file would located at /project/update_settings.json

The settings file must be called "update_settings.json" and in the form:
```json
{
    "UPDATENAME": "REPO_NAME",
    "UPDATEURL": "https://api.github.com/repos/__AUTHOR__/__REPO__/releases",
    "ASSETPATTERN": [
        [
            "__CONSISTENT_RELEASE_PATTERN__"
        ],
        "CONSISTENT_RELEASE_FILE_TYPE"
    ]
}
```
