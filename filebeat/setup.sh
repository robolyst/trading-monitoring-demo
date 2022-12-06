set -ux -o pipefail

ELASTICSEARCH_URL="elasticsearch:9200"

function load_pipeline() {
    echo "Loading pipeline"
    curl -X PUT "${ELASTICSEARCH_URL}/_ingest/pipeline/trader_log_pipeline" -H 'Content-Type: application/json' -T /app/pipeline.json
}

function load_index_template() {
    echo "Loading index template"
    curl -X PUT "${ELASTICSEARCH_URL}/_index_template/trader" -H 'Content-Type: application/json' -T /app/template.json
}

load_pipeline
load_index_template