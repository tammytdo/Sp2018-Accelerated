<!-- 18.4.24 git merge issues-->

# Scraped from terminal during git merge resolution on 18.04.26.10:07



```
git pull upstream master
remote: Counting objects: 157, done.
remote: Compressing objects: 100% (54/54), done.
Receiving objects:  63% (99/157)   ed 101 (delta 58), pack-reused 41
Receiving objects: 100% (157/157), 38.72 KiB | 0 bytes/s, done.
Resolving deltas: 100% (77/77), completed with 22 local objects.
From https://github.com/UWPCE-PythonCert-ClassRepos/Sp2018-Accelerated
 * branch            master     -> FETCH_HEAD
   802f6d5..ec58b02  master     -> upstream/master
Removing students/kristianjf/lesson04/Steve_Jobs.txt
Removing students/kristianjf/lesson04/Jeff_Bezos.txt
Removing students/kristianjf/lesson04/Bill_Gates.txt
Auto-merging students/jayjohnson/lesson02/Grid_Printer.py
CONFLICT (content): Merge conflict in students/jayjohnson/lesson02/Grid_Printer.py
Auto-merging students/Ruohan/lesson02/series.py
CONFLICT (content): Merge conflict in students/Ruohan/lesson02/series.py
Auto-merging students/Ruohan/lesson02/grid_printer_part3.py
CONFLICT (content): Merge conflict in students/Ruohan/lesson02/grid_printer_part3.py
Auto-merging students/Ruohan/lesson02/grid_printer_part2.py
CONFLICT (content): Merge conflict in students/Ruohan/lesson02/grid_printer_part2.py
Auto-merging students/Ruohan/lesson02/fizzbuzz.py
CONFLICT (content): Merge conflict in students/Ruohan/lesson02/fizzbuzz.py
Auto-merging notes_for_class/source/session06.rst
CONFLICT (content): Merge conflict in notes_for_class/source/session06.rst
Automatic merge failed; fix conflicts and then commit the result.
PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>git status
On branch master
Your branch is up-to-date with 'origin/master'.
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:

        modified:   ../../examples/Session05/arbitrary_key.py
        new file:   ../../examples/Session06/cigar_party.py
        new file:   ../../examples/Session06/test_cigar_party.py
        new file:   ../../solutions/Lesson05/.gitignore
        new file:   ../../solutions/Lesson05/dict_set_with_comps_solution.py
        new file:   ../../solutions/Lesson05/except_exercise_solution.py
        new file:   ../../solutions/Lesson05/except_test.py
        new file:   ../../solutions/Lesson05/fizz_buzz_comprehension.py
        new file:   ../../solutions/Lesson05/mailroom_dict_switch.py
        new file:   ../../solutions/Lesson05/safe_input.py
        new file:   ../../solutions/Lesson05/test_mailroom_dict_switch.py
        new file:   ../Osiddiquee/lesson03/.gitignore
        modified:   ../Osiddiquee/lesson03/mailroom2.py
        renamed:    ../example_student/00-README.md -> ../Ruohan/example_student/00-README.md
        renamed:    ../example_student/name_of_exercise/demo_file.py -> ../Ruohan/example_student/name_of_exercise/demo_file.py
        renamed:    ../example_student/name_of_exercise/firstcommit.py -> ../Ruohan/example_student/name_of_exercise/firstcommit.py
        new file:   ../Ruohan/lesson03/list_lab.py
        new file:   ../Ruohan/lesson03/mailroom.py
        new file:   ../Ruohan/lesson03/slicing_lab.py
        new file:   ../Ruohan/lesson03/strformat_lab.py
        new file:   ../Ruohan/lesson04/kata.py
        new file:   ../Ruohan/lesson04/mailroom_part2
        new file:   ../Ruohan/lesson04/mailroom_part2.py
        new file:   ../Ruohan/lesson04/sherlock.txt
        new file:   ../Ruohan/lesson04/sherlock_small.txt
        new file:   ../Ruohan/lesson05/except_exercise.py
        new file:   ../Ruohan/lesson05/except_test.py
        new file:   ../Ruohan/lesson05/mailroom3.py
        new file:   ../jayjohnson/lesson03/exchange_first_last.py
        new file:   ../jayjohnson/lesson03/list_lab.py
        new file:   ../jayjohnson/lesson03/mail.py
        new file:   ../jayjohnson/lesson03/strformat_lab.py
        new file:   ../jayjohnson/lesson04/Mailroom.py
        new file:   ../jayjohnson/lesson04/kata.py
        deleted:    ../kristianjf/lesson04/Bill_Gates.txt
        deleted:    ../kristianjf/lesson04/Jeff_Bezos.txt
        deleted:    ../kristianjf/lesson04/Steve_Jobs.txt
        modified:   ../kristianjf/lesson04/mailroom_2.py

Unmerged paths:
  (use "git add <file>..." to mark resolution)

        both modified:   ../../notes_for_class/source/session06.rst
        both modified:   ../Ruohan/lesson02/fizzbuzz.py
        both modified:   ../Ruohan/lesson02/grid_printer_part2.py
        both modified:   ../Ruohan/lesson02/grid_printer_part3.py
        both modified:   ../Ruohan/lesson02/series.py
        both modified:   ../jayjohnson/lesson02/Grid_Printer.py

PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>git add ../jayjohnson/lesson02/Grid_Printer.py
PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>git add ../Ruohan/lesson02/series.py
PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>../Ruohan/lesson02/grid_printer_part3.py
PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>git add ../Ruohan/lesson02/grid_printer_part3.py
PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>git add ../Ruohan/lesson02/grid_printer_part2.py
PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>git add ../Ruohan/lesson02/fizzbuzz.py
PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>git add ../../notes_for_class/source/session06.rst
PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>git status
On branch master
Your branch is up-to-date with 'origin/master'.
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:

        modified:   ../../examples/Session05/arbitrary_key.py
        new file:   ../../examples/Session06/cigar_party.py
        new file:   ../../examples/Session06/test_cigar_party.py
        modified:   ../../notes_for_class/source/session06.rst
        new file:   ../../solutions/Lesson05/.gitignore
        new file:   ../../solutions/Lesson05/dict_set_with_comps_solution.py
        new file:   ../../solutions/Lesson05/except_exercise_solution.py
        new file:   ../../solutions/Lesson05/except_test.py
        new file:   ../../solutions/Lesson05/fizz_buzz_comprehension.py
        new file:   ../../solutions/Lesson05/mailroom_dict_switch.py
        new file:   ../../solutions/Lesson05/safe_input.py
        new file:   ../../solutions/Lesson05/test_mailroom_dict_switch.py
        new file:   ../Osiddiquee/lesson03/.gitignore
        modified:   ../Osiddiquee/lesson03/mailroom2.py
        renamed:    ../example_student/00-README.md -> ../Ruohan/example_student/00-README.md
        renamed:    ../example_student/name_of_exercise/demo_file.py -> ../Ruohan/example_student/name_of_exercise/demo_file.py
        renamed:    ../example_student/name_of_exercise/firstcommit.py -> ../Ruohan/example_student/name_of_exercise/firstcommit.py
        modified:   ../Ruohan/lesson02/fizzbuzz.py
        modified:   ../Ruohan/lesson02/grid_printer_part2.py
        modified:   ../Ruohan/lesson02/grid_printer_part3.py
        modified:   ../Ruohan/lesson02/series.py
        new file:   ../Ruohan/lesson03/list_lab.py
        new file:   ../Ruohan/lesson03/mailroom.py
        new file:   ../Ruohan/lesson03/slicing_lab.py
        new file:   ../Ruohan/lesson03/strformat_lab.py
        new file:   ../Ruohan/lesson04/kata.py
        new file:   ../Ruohan/lesson04/mailroom_part2
        new file:   ../Ruohan/lesson04/mailroom_part2.py
        new file:   ../Ruohan/lesson04/sherlock.txt
        new file:   ../Ruohan/lesson04/sherlock_small.txt
        new file:   ../Ruohan/lesson05/except_exercise.py
        new file:   ../Ruohan/lesson05/except_test.py
        new file:   ../Ruohan/lesson05/mailroom3.py
        modified:   ../jayjohnson/lesson02/Grid_Printer.py
        new file:   ../jayjohnson/lesson03/exchange_first_last.py
        new file:   ../jayjohnson/lesson03/list_lab.py
        new file:   ../jayjohnson/lesson03/mail.py
        new file:   ../jayjohnson/lesson03/strformat_lab.py
        new file:   ../jayjohnson/lesson04/Mailroom.py
        new file:   ../jayjohnson/lesson04/kata.py
        deleted:    ../kristianjf/lesson04/Bill_Gates.txt
        deleted:    ../kristianjf/lesson04/Jeff_Bezos.txt
        deleted:    ../kristianjf/lesson04/Steve_Jobs.txt
        modified:   ../kristianjf/lesson04/mailroom_2.py

PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>git commit "Still getting merge conflicts with other students work...? used git add filename to resolve and do git pull upstream master."
fatal: cannot do a partial commit during a merge.
PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>git commit -m "Still getting merge conflicts with other students work...? used git add filename to resolve and do git pull upstream master."
[master a97ef00] Still getting merge conflicts with other students work...? used git add filename to resolve and do git pull upstream master.
PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>git push origin master
fatal: HttpRequestException encountered.
   An error occurred while sending the request.
Username for 'https://github.com': mathewcmartin
Password for 'https://mathewcmartin@github.com':
Counting objects: 176, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (94/94), done.
Writing objects: 100% (176/176), 41.58 KiB | 0 bytes/s, done.
Total 176 (delta 90), reused 153 (delta 76)
remote: Resolving deltas: 100% (90/90), completed with 30 local objects.
To https://github.com/mathewcmartin/Sp2018-Accelerated.git
   333c93a..a97ef00  master -> master
PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean
PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm
>git pull upstream master
From https://github.com/UWPCE-PythonCert-ClassRepos/Sp2018-Accelerated
 * branch            master     -> FETCH_HEAD
Already up-to-date.
PS [mattn]D:\uw\Sp2018-Accelerated\students\mathewcm

```
