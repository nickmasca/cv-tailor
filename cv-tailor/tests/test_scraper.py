# filepath: /Users/shucao/cv-tailor/cv-tailor/cv-tailor/tests/test_scraper.py
import pytest
from src.scraper.scraper import Scraper

def test_scrape_from_url_success(mocker):
    # Mock the response from requests.get
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.content = '''
    <html>
        <body>
            <div class="description__text">This is a job description.</div>
        </body>
    </html>
    '''
    mocker.patch('requests.get', return_value=mock_response)

    scraper = Scraper()
    result = scraper.scrape_from_url('http://example.com/job')

    assert result == 'This is a job description.'

def test_scrape_from_url_no_description(mocker):
    # Mock the response from requests.get
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.content = '''
    <html>
        <body>
            <div class="no_description">No job description here.</div>
        </body>
    </html>
    '''
    mocker.patch('requests.get', return_value=mock_response)

    scraper = Scraper()
    result = scraper.scrape_from_url('http://example.com/job')

    assert result == 'Job description not found.'

def test_scrape_from_url_failure(mocker):
    # Mock the response from requests.get
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch('requests.get', return_value=mock_response)

    scraper = Scraper()
    result = scraper.scrape_from_url('http://example.com/job')

    assert result == 'Failed to retrieve the page. Status code: 404'