import pytest
import rdflib

from mskg.surfactant_instance import SurfactantInstance


@pytest.fixture
def instance():
    return SurfactantInstance(chebi_id=71976, id=rdflib.URIRef("http://example.com/test"), name="Surfactin A", wikidata_id="Q27139838")


def test_constructor(instance):
    pass


def test_augment(instance):
    instance.augment()
