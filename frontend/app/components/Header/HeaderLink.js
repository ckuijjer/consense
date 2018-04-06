import { Link } from 'react-router-dom';
import styled from 'styled-components';

export default styled(Link)`
  display: inline-flex;
  padding: 0.2em 0.5em;
  margin: 0.2em;
  text-decoration: none;
  user-select: none;
  cursor: pointer;
  outline: 0;
  font-family: 'Roboto', Roboto, Arial, sans-serif;
  font-weight: bold;
  font-size: 16px;
  color: #57656E;
  border-bottom: 2px solid white;

  &:hover, &:active {
    color: #57656E;
    font-weight: bold;
    border-bottom: 2px solid #59B9AD;
  }
`;
