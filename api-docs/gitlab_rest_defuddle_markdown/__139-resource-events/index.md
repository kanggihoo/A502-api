# Resource events

  ### 3. Resource events API

  • 유용성: P1 (타임라인 및 상태 변경 추적 유용).
      • Issue/MR state events (05~08번): 이슈/MR 상태 변경(Open -> Closed) 타임라인 수집.
      • Label events (11~14번), Milestone events (17~20번): 라벨/마일스톤 변경 이력 추적.
      • Epic / Weight / Iteration events (01~04, 09~10, 15~16번): GitLab Premium/Ultimate (유료
      티어) 전용 기능으로 제외.
  • 티어/권한: 이슈/MR 상태/라벨/마일스톤 이벤트는 Free / CE 지원.
## Endpoints

- [01-Get a list of issue resource iteration events [GET]](./01-get-a-list-of-issue-resource-iteration-events-get.md)
- [02-Get a single issue resource iteration event [GET]](./02-get-a-single-issue-resource-iteration-event-get.md)
- [03-List all project issue weight events [GET]](./03-list-all-project-issue-weight-events-get.md)
- [04-Retrieve single issue weight event [GET]](./04-retrieve-single-issue-weight-event-get.md)
- [05-Get a list of issue resource state events [GET]](./05-get-a-list-of-issue-resource-state-events-get.md)
- [06-Get a single issue resource state event [GET]](./06-get-a-single-issue-resource-state-event-get.md)
- [07-Get a list of merge request resource state events [GET]](./07-get-a-list-of-merge-request-resource-state-events-get.md)
- [08-Get a single merge request resource state event [GET]](./08-get-a-single-merge-request-resource-state-event-get.md)
- [09-Get a list of epic resource state events [GET]](./09-get-a-list-of-epic-resource-state-events-get.md)
- [10-Get a single epic resource state event [GET]](./10-get-a-single-epic-resource-state-event-get.md)
- [11-Get a list of issue resource label events [GET]](./11-get-a-list-of-issue-resource-label-events-get.md)
- [12-Get a single issue resource label event [GET]](./12-get-a-single-issue-resource-label-event-get.md)
- [13-Get a list of merge request resource label events [GET]](./13-get-a-list-of-merge-request-resource-label-events-get.md)
- [14-Get a single merge request resource label event [GET]](./14-get-a-single-merge-request-resource-label-event-get.md)
- [15-Get a list of epic resource label events [GET]](./15-get-a-list-of-epic-resource-label-events-get.md)
- [16-Get a single epic resource label event [GET]](./16-get-a-single-epic-resource-label-event-get.md)
- [17-List project Issue milestone events [GET]](./17-list-project-issue-milestone-events-get.md)
- [18-Get single Issue milestone event [GET]](./18-get-single-issue-milestone-event-get.md)
- [19-List project Merge request milestone events [GET]](./19-list-project-merge-request-milestone-events-get.md)
- [20-Get single Merge request milestone event [GET]](./20-get-single-merge-request-milestone-event-get.md)
