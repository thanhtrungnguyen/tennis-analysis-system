import { Button, Card, Text, Grid } from '@nextui-org/react';
import { useSelector, useDispatch } from 'react-redux';
import { RootState } from '@/app/store/store';
import { logout } from '@/app/features/auth/authSlice';
import { useRouter } from 'next/router';
import withAuth from '@/app/components/hoc/withAuth';

const ManagementPage = () => {
  const { user } = useSelector((state: RootState) => state.auth);
  const dispatch = useDispatch();
  const router = useRouter();

  const handleLogout = () => {
    dispatch(logout());
    router.push('/login'); // Redirect to login after logout
  };

  return (
    <Grid.Container gap={2} justify="center">
      <Grid xs={12} sm={6}>
        <Card>
          <Card.Body>
            <Text h3>Welcome to Management, {user}!</Text>
            <Button color="secondary" onClick={handleLogout}>Logout</Button>
          </Card.Body>
        </Card>
      </Grid>
    </Grid.Container>
  );
};

// Wrap ManagementPage with the withAuth HOC
export default withAuth(ManagementPage);