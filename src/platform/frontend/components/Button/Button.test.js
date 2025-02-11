import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import Button from './Button';

test('Button renders with children and handles click', () => {
    const handleClick = jest.fn();
    const { getByText } = render(<Button onClick={handleClick}>Click Me</Button>);
    const button = getByText('Click Me');
    fireEvent.click(button);
    expect(handleClick).toHaveBeenCalledTimes(1);
});
