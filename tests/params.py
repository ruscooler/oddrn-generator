from oddrn_generator.generators import (
    PostgresqlGenerator, MysqlGenerator, SnowflakeGenerator, AirflowGenerator, HiveGenerator, GlueGenerator,
    DynamodbGenerator, OdbcGenerator, MssqlGenerator, OracleGenerator, RedshiftGenerator, ClickHouseGenerator,
    KafkaConnectGenerator, KafkaGenerator, AthenaGenerator, QuicksightGenerator, TableauGenerator, PrefectGenerator,
    Neo4jGenerator, FeastGenerator
)

parameters_host = [
    (
        PostgresqlGenerator,
        {
            'host_settings': '127.0.0.1:5034',
            'paths': {
                'schemas': 'some_schema',
                'databases': 'some_database',
                'tables': 'some_table',
                'columns': 'some_column',
            },
            'aliases': {}
        }
    ),
    (
        MysqlGenerator,
        {
            'host_settings': '127.0.0.1:5034',
            'paths': {
                'databases': 'some_database',
                'tables': 'some_table',
                'columns': 'some_column',
            },
            'aliases': {}
        }
    ),
    (
        SnowflakeGenerator,
        {
            'host_settings': '127.0.0.1:5034',
            'paths': {
                'warehouses': 'some_warehouse',
                'databases': 'some_database',
                'schemas': 'some_schema',
                'tables': 'some_table',
                'views': 'some_view',
                'columns': 'some_column',
                'owners': 'some_owner',
            },
            'aliases': {}
        }
    ),
    (
        AirflowGenerator,
        {
            'host_settings': '127.0.0.1:5034',
            'paths': {
                'dags': 'some_dag',
                'tasks': 'some_task',
                'runs': 'some_run',
            },
            'aliases': {}
        }
    ),
    (
        HiveGenerator,
        {
            'host_settings': '127.0.0.1:5034',
            'paths': {
                'databases': 'some_database',
                'tables': 'some_table',
                'columns': 'some_column',
                'owners': 'some_owner',
            },
            'aliases': {}
        }
    ),
    (
        OdbcGenerator,
        {
            'host_settings': '127.0.0.1:5034',
            'paths': {
                'databases': 'some_database',
                'schemas': 'some_schema',
                'tables': 'some_table',
                'columns': 'some_column',
            },
            'aliases': {}
        }
    ),
    (
        MssqlGenerator,
        {
            'host_settings': '127.0.0.1:5034',
            'paths': {
                'databases': 'some_database',
                'schemas': 'some_schema',
                'tables': 'some_table',
                'columns': 'some_column',
            },
            'aliases': {}
        }
    ),
    (
        OracleGenerator,
        {
            'host_settings': '127.0.0.1:5034',
            'paths': {
                'databases': 'some_database',
                'schemas': 'some_schema',
                'tables': 'some_table',
                'columns': 'some_column',
            },
            'aliases': {}
        }
    ),
    (
        RedshiftGenerator,
        {
            'host_settings': '127.0.0.1:5034',
            'paths': {
                'databases': 'some_database',
                'schemas': 'some_schema',
                'tables': 'some_table',
                'columns': 'some_column',
            },
            'aliases': {}
        }
    ),
    (
        ClickHouseGenerator,
        {
            'host_settings': '127.0.0.1:5034',
            'paths': {
                'databases': 'some_database',
                'tables': 'some_table',
                'columns': 'some_column',
            },
            'aliases': {}
        }
    ),
    (
        KafkaGenerator,
        {
            'host_settings': '127.0.0.1:5034',
            'paths': {
                'topics': 'some_topics',
            },
            'aliases': {}
        }
    ),
    (
        KafkaConnectGenerator,
        {
            'host_settings': '127.0.0.1:5034',
            'paths': {
                'connectors': 'some_connector',
            },
            'aliases': {}
        }
    ),
    (
        TableauGenerator,
        {
            'host_settings': 'dub01.online.tableau.com',
            'paths': {
                'sites': 'some_site',
                'databases': 'some_database',
                'schemas': 'some_schema',
                'tables': 'some_table',
                'columns': 'some_column',
                'workbooks': 'some_workbook',
                'sheets': 'some_sheet',
            },
            'aliases': {}
        }
    ),
    (
        PrefectGenerator,
        {
            'host_settings': '127.0.0.1:5034',
            'paths': {
                'flows': 'some_flow',
                'tasks': 'some_task',
                'runs': 'some_run',
            },
            'aliases': {}
        }
    ),
    (
        Neo4jGenerator,
        {
            'host_settings': '127.0.0.1:9687',
            'paths': {
                'databases': 'some_database',
                'nodes': 'some_node',
            },
            'aliases': {}
        }
    ),
    (
        FeastGenerator,
        {
            'host_settings': 'feast_unit_id',
            'paths': {
                'featureviews': 'some_featureviews',
                'features': 'some_features',
                'subfeatures': 'some_subfeatures',
            },
            'aliases': {}
        }
    ),
]

parameters_cloud = [
    (
        GlueGenerator,
        {
            'cloud_settings': {
                'account': '21232132',
                'region': 'us-west',
            },
            'paths': {
                'databases': 'some_database',
                'tables': 'some_table',
                'columns': 'some_column',
                'owners': 'some_owner',
                'jobs': 'some_jobs',
                'runs': 'some_runs',
            },
            'aliases': {}
        }
    ),
    (
        DynamodbGenerator,
        {
            'cloud_settings': {
                'account': '21232132',
                'region': 'us-west',
            },
            'paths': {
                'tables': 'some_table',
                'columns': 'some_column',
            },
            'aliases': {}
        }
    ),
    (
        AthenaGenerator,
        {
            'cloud_settings': {
                'account': '21232132',
                'region': 'us-west',
            },
            'paths': {
                'catalogs': 'some_catalog',
                'databases': 'some_database',
                'tables': 'some_table',
                'columns': 'some_column',
            },
            'aliases': {}
        }
    ),
    (
        QuicksightGenerator,
        {
            'cloud_settings': {
                'account': '21232132',
                'region': 'us-west',
            },
            'paths': {
                'datasets': 'some_dataset',
                'analyses': 'some_analysis',
                'dashboards': 'some_dashboard',
                'data_sources': 'some_data_sources',
            },
            'aliases': {}
        }
    ),
]
