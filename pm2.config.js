module.exports = {
  apps: [
    {
      name: 'Django',
      script: 'manage.py',
      args: ['runserver', '172.31.9.162:8989'],
      interpreter: 'python3',
      watch: false,
      autorestart: true,
      max_restarts: 10,
      instances: 1,
      exec_mode: 'fork',
    },
  ],
};
