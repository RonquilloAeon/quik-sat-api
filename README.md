A simple FastAPI API that returns Starlink satellite data.

The is the source code for the tutorial *Python FastAPI Tutorial - Building a Satellite API*. 
See the tutorial: https://youtu.be/StHtw2YvNFU

## Building/running container
- For developing, run `docker-compose up`.
- For building locally, run `docker build --target production -t quik-sat .` then run `docker run -p 8080:8080 --env "SATELLITE_REPOSITORY_URL=https://www.celestrak.com/NORAD/elements/starlink.txt" --env "PORT=8080" -it quik-sat`
- To build with Cloud Run: `gcloud builds submit --config cloudbuild.yml`
