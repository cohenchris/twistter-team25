import React from 'react';
import ReactDOM from 'react-dom';
import DmPage from './DmPage';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<DmPage />, div);
  ReactDOM.unmountComponentAtNode(div);
});
