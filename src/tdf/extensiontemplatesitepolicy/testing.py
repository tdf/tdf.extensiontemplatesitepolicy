from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class TdfextensiontemplatesitepolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import tdf.extensiontemplatesitepolicy
        xmlconfig.file(
            'configure.zcml',
            tdf.extensiontemplatesitepolicy,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tdf.extensiontemplatesitepolicy:default')

TDF_EXTENSIONTEMPLATESITEPOLICY_FIXTURE = TdfextensiontemplatesitepolicyLayer()
TDF_EXTENSIONTEMPLATESITEPOLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TDF_EXTENSIONTEMPLATESITEPOLICY_FIXTURE,),
    name="TdfextensiontemplatesitepolicyLayer:Integration"
)
TDF_EXTENSIONTEMPLATESITEPOLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TDF_EXTENSIONTEMPLATESITEPOLICY_FIXTURE, z2.ZSERVER_FIXTURE),
    name="TdfextensiontemplatesitepolicyLayer:Functional"
)
