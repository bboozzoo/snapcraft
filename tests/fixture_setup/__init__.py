import os
import socket

if hasattr(socket, "AF_UNIX"):
    from ._unix import FakeSnapd  # noqa: F401
try:
    from ._unittests import (  # noqa: F401
        FakeAptBaseDependency,
        FakeAptCache,
        FakeAptCachePackage,
        FakeElf,
        FakeExtension,
        FakeMetadataExtractor,
        FakePlugin,
        FakeProjectOptions,
        FakeSnapCommand,
        FakeSnapcraftctl,
        FakeMultipass,
        SilentSnapProgress,
    )
except ImportError as import_error:
    if os.path.exists(os.path.join(os.path.dirname(__file__), "..", "snapcraft")):
        raise import_error

from ._fixtures import (  # noqa: F401
    BzrRepo,
    CleanEnvironment,
    FakeBaseEnvironment,
    FakeParts,
    FakePartsServerRunning,
    FakePartsWiki,
    FakePartsWikiOrigin,
    FakePartsWikiOriginRunning,
    FakePartsWikiRunning,
    FakePartsWikiWithSlashes,
    FakePartsWikiWithSlashesRunning,
    FakePlatformRepo,
    FakeSSOServerRunning,
    FakeServerRunning,
    FakeSnapcraftIsASnap,
    FakeStore,
    FakeStoreAPIServerRunning,
    FakeStoreSearchServerRunning,
    FakeStoreUploadServerRunning,
    FakeTerminal,
    GitRepo,
    HgRepo,
    SharedCache,
    SnapcraftYaml,
    StagingStore,
    SvnRepo,
    TempCWD,
    TempXDG,
    TestStore,
    WithoutSnapInstalled,
)
