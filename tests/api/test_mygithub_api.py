import pytest


@pytest.mark.api
def test_search_users_by_location_in_profile(github_api):
    r = github_api.search_users('location:Lviv')
    #print(r)
    assert r['total_count'] <= 10000


@pytest.mark.api
def test_search_no_users_by_unexist_location(github_api):
    r = github_api.search_users('location:Nenatsk')
    assert r['total_count'] == 0


@pytest.mark.api
def test_search_users_by_empty_location_shows_allusers(github_api):
    r = github_api.search_users('location:   ')
    # print(r)
    assert r['total_count'] >= 80000000




@pytest.mark.api
def test_branch_master_exist(github_api):
    r = github_api.get_branch('milakul', 'MilaQA', 'master')
    assert r['name'] == 'main'


@pytest.mark.api
def test_branch_not_exist(github_api):
    r = github_api.get_branch('milakul', 'MilaQA', 'nosuchbranch')
    assert r['message'] == 'Branch not found' 



