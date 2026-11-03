"""The app's version, in one place.

The updater compares this against the newest GitHub release, so it has to be
the same number the exe reports in its own properties. build_exe.py checks
version_info.txt against it and refuses to build if they have drifted -- a
build that ships as 1.4.0 while telling the updater it is 1.3.2 would offer
every user an update to the version they are already running.
"""

APP_VERSION = "1.27.1"

# Where updates come from. Hardcoded on purpose: the page must never be able
# to point the updater at a different repository.
# Empty in this Philibert build: an update from the original project would replace
# it with a version that sends transcripts to the cloud.
UPDATE_REPO = ""
