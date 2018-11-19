import json
import logging

from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class PostgresToFileOperator(BaseOperator):
    """
    Executes sql code in a specific Postgres database
    :param postgres_conn_id: reference to a specific postgres database
    :type postgres_conn_id: string
    :param sql: the sql code to be executed
    :type sql: Can receive a str representing a sql statement,
        a list of str (sql statements), or reference to a template file.
        Template reference are recognized by str ending in '.sql'
    """

    template_fields = ('sql', 'parameters', 'location')
    template_ext = ('.sql',)
    ui_color = '#ededed'

    @apply_defaults
    def __init__(
            self,
            sql,
            parameters=None,
            location='/usr/local/airflow/datalake',
            conn_id='postgres_default',
            *args, **kwargs):
        super(PostgresToFileOperator, self).__init__(*args, **kwargs)
        self.sql = sql
        self.conn_id = conn_id
        self.location = location
        self.parameters = parameters

    def execute(self, context):
        logging.info('Executing: ' + str(self.sql))
        pg_hook = PostgresHook(postgres_conn_id=self.conn_id)

        conn = pg_hook.get_conn()
        cursor = conn.cursor()
        cursor.execute(self.sql, self.parameters)

        with open(self.location, 'w') as f:
            fields = [field[0] for field in cursor.description]
            for row in cursor:
                line = {}
                for key, value in zip(fields, row):
                    line[key] = value
                f.write(json.dumps(line))
                f.write('\n')

        logging.info("Done.")