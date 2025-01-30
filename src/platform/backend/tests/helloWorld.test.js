const helloWorld = require('../helloWorld');

test('hello world!', () => {
    expect(helloWorld()).toBe('Hello, World!');
});
