import styled from 'tailwind';

const StyledAuth = styled.div`
  color: pink;
`;

export function Auth() {
  return (
    <StyledAuth>
      <h1>Welcome to Auth!</h1>
    </StyledAuth>
  );
}

export default Auth;
