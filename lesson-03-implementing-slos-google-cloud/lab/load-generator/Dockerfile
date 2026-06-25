FROM alpine:3.19

RUN apk add --no-cache curl bash

COPY generate-traffic.sh /generate-traffic.sh
RUN chmod +x /generate-traffic.sh

CMD ["/generate-traffic.sh"]
