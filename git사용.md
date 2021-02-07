my git: https://github.com/rsentra/myProj.git   => origin/master 
- 한글깨짐 방지  
git config --global core.quotepath false 

### 1. git status : 연결상태, unstaged source있는지 확인  
### 2. 소스를 편집,변경  
### 3. staging: git add <file name>   또는 git add -all  
4. commit : git commit -m "commit msessage~~"  
5. pull : git pull origin master  
6: push : git push origin master  
 
■ git 상태  
git status 
git status 'file name' : 특정파일의 git상태보기
 
■ git staging 
 -- git add all 
 git add . 
 --git add 취소 all 
 git rm -rf --cached . 
 -- git add 취소 file 
 git rm --cached 'file name' 
 git reset HEAD 'file name' 
  
■ git commit 조회 
git show : 현재 브랜치의 가장 최근 커밋 정보를 확인함 
git show 커밋해시값 : 특정 커밋 정보를 확인함 
git show HEAD : HEAD 포인터가 가리키는 커밋정보를 확인함 
git show 커밋해시값 또는 HEAD^ 

 --push하지 않은 커밋 표시 
 git log --branches --not --remotes 
  
-- git commit 취소 
 [방법 1] commit을 취소하고 해당 파일들은 staged 상태로 워킹 디렉터리에 보존
 git reset --soft HEAD^
 [방법 2] commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉터리에 보존
  git reset --mixed HEAD^ # 기본 옵션
  git reset HEAD^ # 위와 동일
  git reset HEAD~2 # 마지막 2개의 commit을 취소
 [방법 3] commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉터리에서 삭제
  git reset --hard HEAD^
https://gmlwjd9405.github.io/2018/05/25/git-add-cancle.html

■ git 관리 
 --git에 잘못올라간 파일삭제 -> commit -> push
 git rm --cached [File Name]      # 파일삭제
 git rm --cached  -r [dirname/]   # dir및 파일삭제
  
 --git + local모두 삭제 -> commit -> push
 git rm [File Name]
 
■ git ignore
 gitignore 설정: 파일편집->file name추가
 
 [ignore 문법] 
 - comments 표시는 # 
 -  no .a files 
   *.a   
 -  but do track lib.a, even though you're ignoring .a files above 
    !lib.a 
 - only ignore the TODO file in the current directory, not subdir/TODO 
    /TODO 
 - ignore all files in the build/ directory 
    build/ 
 - ignore doc/notes.txt, but not doc/server/arch.txt 
    doc/*.txt 
 - ignore all .pdf files in the doc/ directory 
   doc/**/*.pdf 
 
 ---------------------------
 git에 관한 책 
 https://wikidocs.net/book/1902 