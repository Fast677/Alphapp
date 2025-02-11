import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import Modal from './Modal';

test('Modal renders when open and handles close', () => {
    const handleClose = jest.fn();
    const { getByText, queryByText } = render(
        <Modal isOpen={true} onClose={handleClose}>
            Modal Content
        </Modal>
    );
    const modalContent = getByText('Modal Content');
    expect(modalContent).toBeInTheDocument();

    const closeButton = getByText('X');
    fireEvent.click(closeButton);
    expect(handleClose).toHaveBeenCalledTimes(1);
});
