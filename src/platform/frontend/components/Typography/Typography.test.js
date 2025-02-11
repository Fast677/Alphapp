import React from 'react';
import { render } from '@testing-library/react';
import Typography from './Typography';

test('Typography renders with correct variant', () => {
    const { getByText } = render(<Typography variant="h1">Heading</Typography>);
    const heading = getByText('Heading');
    expect(heading.tagName).toBe('H1');
});
