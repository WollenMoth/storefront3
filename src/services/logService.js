import * as Sentry from "@sentry/react";
import { Integrations } from "@sentry/tracing";

function init() {
  Sentry.init({
    dsn: "https://fd0bb716b6334e5db51b7eff243d2137@o1113861.ingest.sentry.io/6180432",
    integrations: [new Integrations.BrowserTracing()],
    environment: "development",
    tracesSampleRate: 1.0,
  });
}

function log(error) {
  Sentry.captureException(error);
}

const exportedObj = {
  init,
  log,
};

export default exportedObj;
