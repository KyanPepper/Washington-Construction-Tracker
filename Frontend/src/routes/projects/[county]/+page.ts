import type { PageLoad } from './$types';
export const load: PageLoad = async ({ fetch,params }) => {
  try {
    let endpoint;
    if (params.county === 'Snohomish'){
        endpoint = 'getSno'
    }else if(params.county === 'King'){
        endpoint = 'getKing'
    }else if(params.county === 'Spokane'){
        endpoint = 'getSpo'
    }else if(endpoint = 'Other'){
        endpoint = 'getNC'
    }else{
        endpoint = 'getAll'
    }
    const response = await fetch(`http://127.0.0.1:5000/getproject/${endpoint}`);
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
