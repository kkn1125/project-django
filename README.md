# project-django

django

## 브랜치 운영 필독

> 브랜치 운영에 실무에서 사용하는 것을 익혀보기 위해 틀린 부분이 있어도 더 나은 방법을 강구하기 위해 해당 사항을 준수하기를 당부 함. 불편하더라도 익숙해지면 이후 수월해 질 것으로 생각.

1. `main` 브랜치는 `master`브랜치로 절대 `main` 브랜치로 병합하는 일이 없어야 한다.
2. `main`브랜치는 `develop` 브랜치를 통해 업데이트 되며, 모든 작업은 **pull request**로 확인 후 `develop`브랜치로 **merge** 과정을 밟도록 한다.
3. 브랜치 명명 규칙은 `행위/이슈넘버-작업사항/아이디` 혹은 `행위/작업사항/아이디` 아래와 같다.
   1. **feature**/3-login/*kimson* `(기능 추가)`
   2. **bugfix**/4-users/*ohoraming* `(버그 수정)`
   3. **update**/db_table/*kimson* `(기타 수정)`
4. 코드 변경사항 확인 후 `review`표시 혹은 fetch & merge(pull) 후 테스트 결과 의견 첨부(필요 시)

## update list

업데이트 내역은 이슈에 다는 것으로!

## authors

[@kimson](https://github.com/kkn1125), [@ohoraming](https://github.com/ohoraming)