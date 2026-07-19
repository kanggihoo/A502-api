---
title: "Webhook administration Rake tasks"
source: "https://docs.gitlab.com/administration/raketasks/web_hooks/"
created: 2026-07-20
description: "GitLab 제품 문서."
---

/

---

GitLab은 웹훅 관리를 위한 Rake 작업을 제공합니다.

웹훅의 [로컬 네트워크 요청](https://docs.gitlab.com/security/webhooks/)은 관리자가 허용하거나 차단할 수 있습니다.

## 모든 프로젝트에 웹훅 추가

모든 프로젝트에 웹훅을 추가하려면 다음을 실행하세요:

```shell
# omnibus-gitlab
sudo gitlab-rake gitlab:web_hook:add URL="http://example.com/hook"

# source installations
bundle exec rake gitlab:web_hook:add URL="http://example.com/hook" RAILS_ENV=production
```

## 네임스페이스 내 프로젝트에 웹훅 추가

특정 네임스페이스의 모든 프로젝트에 웹훅을 추가하려면 다음을 실행하세요:

```shell
# omnibus-gitlab
sudo gitlab-rake gitlab:web_hook:add URL="http://example.com/hook" NAMESPACE=<namespace>

# source installations
bundle exec rake gitlab:web_hook:add URL="http://example.com/hook" NAMESPACE=<namespace> RAILS_ENV=production
```

## 프로젝트에서 웹훅 제거

모든 프로젝트에서 웹훅을 제거하려면 다음을 실행하세요:

```shell
# omnibus-gitlab
sudo gitlab-rake gitlab:web_hook:rm URL="http://example.com/hook"

# source installations
bundle exec rake gitlab:web_hook:rm URL="http://example.com/hook" RAILS_ENV=production
```

## 네임스페이스 내 프로젝트에서 웹훅 제거

특정 네임스페이스의 프로젝트에서 웹훅을 제거하려면 다음을 실행하세요:

```shell
# omnibus-gitlab
sudo gitlab-rake gitlab:web_hook:rm URL="http://example.com/hook" NAMESPACE=<namespace>

# source installations
bundle exec rake gitlab:web_hook:rm URL="http://example.com/hook" NAMESPACE=<namespace> RAILS_ENV=production
```

## 모든 웹훅 목록 보기

모든 웹훅을 나열하려면 다음을 실행하세요:

```shell
# omnibus-gitlab
sudo gitlab-rake gitlab:web_hook:list

# source installations
bundle exec rake gitlab:web_hook:list RAILS_ENV=production
```

## 네임스페이스 내 프로젝트의 웹훅 목록 보기

특정 네임스페이스의 프로젝트에 대한 모든 웹훅을 나열하려면 다음을 실행하세요:

```shell
# omnibus-gitlab
sudo gitlab-rake gitlab:web_hook:list NAMESPACE=<namespace>

# source installations
bundle exec rake gitlab:web_hook:list NAMESPACE=<namespace> RAILS_ENV=production
```
