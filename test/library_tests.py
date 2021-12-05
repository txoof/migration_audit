#!/usr/bin/env python3
# coding: utf-8




import logging
import pytest 
from migration_audit.library import GDrive

import oauth2client

logger = logging.getLogger(__name__)
logger.root.setLevel('DEBUG')






@pytest.fixture
def googledrive():
    return GDrive.GoogleDrive()

def test_test():
    assert 2 == 5

def test_GDriveError():
    with pytest.raises(GDrive.GDriveError) as e_info:
        raise GDrive.GDriveError('GDrive Exception')
    assert e_info.value.args[0] == 'GDrive Exception'

def test_GDriveNetworkError():
    with pytest.raises(GDrive.GDriveNetworkError) as e_info:
        raise GDrive.GDriveNetworkError('GDrive Network Exception')
    assert e_info.value.args[0] == 'GDrive Network Exception'


def test_retry_decorator():
    assert callable(GDrive.retryer())

def test_GoogleDrive_constructor(googledrive):
    assert isinstance(googledrive, GDrive.GoogleDrive)
    
def test_fail():
    assert 2==8




