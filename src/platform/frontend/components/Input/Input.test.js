import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import Input from './Input';

test('Input renders with value and handles change', () => {
    const handleChange = jest.fn();
    const { getByPlaceholderText } = render(
        <Input value="test" onChange={handleChange} placeholder="Enter text" />
    );
    const input = getByPlaceholderText('Enter text');
    fireEvent.change(input, { target: { value: 'new value' } });
    expect(handleChange).toHaveBeenCalledTimes(1);
});
