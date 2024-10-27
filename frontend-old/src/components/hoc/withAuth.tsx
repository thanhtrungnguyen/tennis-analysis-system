import { useEffect } from 'react';
import { useSelector } from 'react-redux';
import { useRouter } from 'next/router';
import { RootState } from '@/app/store/store';

const withAuth = (WrappedComponent: React.ComponentType) => {
  const AuthenticatedComponent = (props: any) => {
    const router = useRouter();
    const isAuthenticated = useSelector((state: RootState) => state.auth.isAuthenticated);

    useEffect(() => {
      if (!isAuthenticated) {
        router.push('/login'); // Redirect to login if not authenticated
      }
    }, [isAuthenticated, router]);

    // Render nothing while redirecting
    if (!isAuthenticated) {
      return null;
    }

    return <WrappedComponent {...props} />;
  };

  return AuthenticatedComponent;
};

export default withAuth;