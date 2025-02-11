import React from 'react';
import './Typography.css';

const Typography = ({ variant, children }) => {
    const Tag = variant || 'p';
    return <Tag className={`typography ${variant}`}>{children}</Tag>;
};

export default Typography;
