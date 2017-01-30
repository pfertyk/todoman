from todoman.cli import cli


def test_list_all(tmpdir, runner, create):
    create(
        'test.ics',
        'SUMMARY:Do stuff\n'
        'STATUS:COMPLETED\n'
        'DUE;VALUE=DATE-TIME;TZID=ART:20160102T000000\n'
        'PERCENT-COMPLETE:26\n'
    )

    result = runner.invoke(cli, ['--porcelain', 'list', '--all'])
    assert (
        result.output.strip() ==
        '{"completed": true, "due": 1451703600, "id": 1, "list": "default'
        '", "percent": 26, "summary": "Do stuff", "urgent": false}'
    )


def test_list_nodue(tmpdir, runner, create):
    create(
        'test.ics',
        'SUMMARY:Do stuff\n'
        'PERCENT-COMPLETE:12\n'
        'PRIORITY:1\n'
    )

    result = runner.invoke(cli, ['--porcelain', 'list'])
    assert (
        result.output.strip() ==
        '{"completed": false, "due": null, "id": 1, "list": "default'
        '", "percent": 12, "summary": "Do stuff", "urgent": true}'
    )
