from todoman.model import Database


def test_save(tmpdir, runner, create, generate, compare):
    name = 'test.ics'
    content = (
        'SUMMARY:harhar\n'
        'UID:rawr\n'
        # TODO: also test UID first
    )
    create(name, content)

    db = Database(str(tmpdir.join('default')))
    todo = list(db.todos.values())[0]

    db.save(todo)

    assert compare(name, content)
