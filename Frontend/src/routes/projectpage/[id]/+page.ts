import type { PageLoad } from './$types';
export const load: PageLoad = async ({ fetch,params }) => {
  try {
    const response = await fetch(`http://127.0.0.1:5000/getproject/${params.id}`);
    if (!response.ok) {
      throw new Error(`Failed to fetch data: ${response.status}`);
    }
    const data = await response.json();
    return { project: data };
  } catch (error) {
    console.error('Error fetching random projects during SSR:', error);
    return { project: null };
  }
};
