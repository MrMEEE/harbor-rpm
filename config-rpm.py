import sys
import os
from os import path
from pathlib import Path
from utils.misc import generate_random_string

from utils.misc import delfile
from utils.configs import validate, parse_yaml_config
from utils.cert import prepare_ca, SSL_CERT_KEY_PATH, SSL_CERT_PATH, get_secret_key
from utils.db import prepare_db
from utils.jobservice import prepare_job_service
from utils.registry import prepare_registry
from utils.registry_ctl import prepare_registry_ctl
from utils.core import prepare_core
from utils.notary import prepare_notary
from utils.log import prepare_log_configs
from utils.clair import prepare_clair
from utils.chart import prepare_chartmuseum
from utils.docker_compose import prepare_docker_compose
from utils.nginx import prepare_nginx, nginx_confd_dir
from g import (config_dir, input_config_path, private_key_pem_path, root_crt_path, secret_key_dir,
old_private_key_pem_path, old_crt_path)

def main():
    if not path.exists("/etc/harbor/secret/registry/root.crt"):
        core_secret = generate_random_string(16)
        jobservice_secret = generate_random_string(16)
        os.system("sed -i 's/^CORE_SECRET=.*$/CORE_SECRET={}/g' /etc/harbor/core/env".format(core_secret))
        os.system("sed -i 's/^JOBSERVICE_SECRET=.*$/JOBSERVICE_SECRET={}/g' /etc/harbor/core/env".format(jobservice_secret))
        os.system("sed -i 's/^CORE_SECRET=.*$/CORE_SECRET={}/g' /etc/harbor/jobservice/env".format(core_secret))
        os.system("sed -i 's/^JOBSERVICE_SECRET=.*$/JOBSERVICE_SECRET={}/g' /etc/harbor/jobservice/env".format(jobservice_secret))
        os.system("sed -i 's/^CORE_SECRET=.*$/CORE_SECRET={}/g' /etc/harbor/registryctl/env".format(core_secret))
        os.system("sed -i 's/^JOBSERVICE_SECRET=.*$/JOBSERVICE_SECRET={}/g' /etc/harbor/registryctl/env".format(jobservice_secret))

    get_secret_key("/etc/harbor/secret/keys/")

    private_key_pem_path=Path("/etc/harbor/secret/core/private_key.pem")
    root_crt_path=Path("/etc/harbor/secret/registry/root.crt")
    #  If Customized cert enabled
    prepare_ca(
        private_key_pem_path=private_key_pem_path,
        root_crt_path=root_crt_path,
        old_private_key_pem_path=old_private_key_pem_path,
        old_crt_path=old_crt_path)
    os.system("chown harbor:harbor -R /etc/harbor/secret/")
if __name__ == '__main__':
    main()
