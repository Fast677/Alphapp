import React from 'react';
import { render } from '@testing-library/react';
import Card from './Card';

test('Card renders with children', () => {
    const { getByText } = render(<Card>Card Content</Card>);
    const cardContent = getByText('Card Content');
    expect(cardContent).toBeInTheDocument();
});
