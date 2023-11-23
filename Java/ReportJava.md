SonarLint 
Executing c:\Users\sench\.vscode\extensions\sonarsource.sonarlint-vscode-4.1.0-win32-x64\jre\21.0.1-win32-x86_64.tar\bin\java -jar c:\Users\sench\.vscode\extensions\sonarsource.sonarlint-vscode-4.1.0-win32-x64\server\sonarlint-ls.jar -stdio -analyzers c:\Users\sench\.vscode\extensions\sonarsource.sonarlint-vscode-4.1.0-win32-x64\analyzers\sonargo.jar c:\Users\sench\.vscode\extensions\sonarsource.sonarlint-vscode-4.1.0-win32-x64\analyzers\sonarjava.jar c:\Users\sench\.vscode\extensions\sonarsource.sonarlint-vscode-4.1.0-win32-x64\analyzers\sonarjs.jar c:\Users\sench\.vscode\extensions\sonarsource.sonarlint-vscode-4.1.0-win32-x64\analyzers\sonarphp.jar c:\Users\sench\.vscode\extensions\sonarsource.sonarlint-vscode-4.1.0-win32-x64\analyzers\sonarpython.jar c:\Users\sench\.vscode\extensions\sonarsource.sonarlint-vscode-4.1.0-win32-x64\analyzers\sonarhtml.jar c:\Users\sench\.vscode\extensions\sonarsource.sonarlint-vscode-4.1.0-win32-x64\analyzers\sonarxml.jar c:\Users\sench\.vscode\extensions\sonarsource.sonarlint-vscode-4.1.0-win32-x64\analyzers\sonarcfamily.jar c:\Users\sench\.vscode\extensions\sonarsource.sonarlint-vscode-4.1.0-win32-x64\analyzers\sonartext.jar c:\Users\sench\.vscode\extensions\sonarsource.sonarlint-vscode-4.1.0-win32-x64\analyzers\sonariac.jar c:\Users\sench\.vscode\extensions\sonarsource.sonarlint-vscode-4.1.0-win32-x64\analyzers\sonarlintomnisharp.jar
[Info  - 16:03:43.487] Started embedded server on port 64120
[Info  - 16:03:47.002] Analyzing file "file:///c:/Coding/SM%20Assiment1/HelloWorld.java"...
[Info  - 16:04:13.580] Found 1 issue
[Info  - 16:04:13.581] Analyzing file "file:///c:/Coding/SM%20Assiment1/HelloWorld.java"...
[Info  - 16:04:14.488] Found 15 issues
[Info  - 16:10:36.492] Analyzing file "file:///c:/Coding/SM%20Assiment1/Java/HelloWorld.java"...
[Info  - 16:10:36.711] Found 15 issues
[Info  - 16:14:14.017] Analyzing file "file:///c:/Coding/SM%20Assiment1/Java/google_checks.xml"...
[Info  - 16:14:14.346] Found 0 issues
[Info  - 16:18:51.085] Analyzing file "file:///c:/Coding/SM%20Assiment1/Java/HelloWorld.java"...
[Info  - 16:18:51.289] Found 15 issues

[{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S1220",
	"severity": 4,
	"message": "Move this file to a named package.",
	"source": "sonarlint",
	"startLineNumber": 1,
	"startColumn": 1,
	"endLineNumber": 1,
	"endColumn": 1
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S1128",
	"severity": 4,
	"message": "Remove this unused import 'java.io.IOException'.",
	"source": "sonarlint",
	"startLineNumber": 3,
	"startColumn": 8,
	"endLineNumber": 3,
	"endColumn": 27
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S1128",
	"severity": 4,
	"message": "Remove this unused import 'java.io.PrintStream'.",
	"source": "sonarlint",
	"startLineNumber": 5,
	"startColumn": 8,
	"endLineNumber": 5,
	"endColumn": 27
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S1450",
	"severity": 4,
	"message": "Remove the \"instance\" field and declare it as a local variable in the relevant methods.",
	"source": "sonarlint",
	"startLineNumber": 8,
	"startColumn": 28,
	"endLineNumber": 8,
	"endColumn": 36
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S1068",
	"severity": 4,
	"message": "Remove this unused \"instance\" private field.",
	"source": "sonarlint",
	"startLineNumber": 8,
	"startColumn": 28,
	"endLineNumber": 8,
	"endColumn": 36
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S112",
	"severity": 4,
	"message": "Define and throw a dedicated exception instead of using a generic one.",
	"source": "sonarlint",
	"startLineNumber": 25,
	"startColumn": 17,
	"endLineNumber": 25,
	"endColumn": 33
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S6548",
	"severity": 4,
	"message": "A Singleton implementation was detected. Make sure the use of the Singleton pattern is required and the implementation is the right one for the context. [+1 location]",
	"source": "sonarlint",
	"startLineNumber": 30,
	"startColumn": 7,
	"endLineNumber": 30,
	"endColumn": 20
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S6548",
	"severity": 4,
	"message": "A Singleton implementation was detected. Make sure the use of the Singleton pattern is required and the implementation is the right one for the context. [+1 location]",
	"source": "sonarlint",
	"startLineNumber": 42,
	"startColumn": 7,
	"endLineNumber": 42,
	"endColumn": 27
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S112",
	"severity": 4,
	"message": "Define and throw a dedicated exception instead of using a generic one.",
	"source": "sonarlint",
	"startLineNumber": 51,
	"startColumn": 14,
	"endLineNumber": 51,
	"endColumn": 30
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S4719",
	"severity": 4,
	"message": "Replace charset name argument with StandardCharsets.UTF_8",
	"source": "sonarlint",
	"startLineNumber": 71,
	"startColumn": 89,
	"endLineNumber": 71,
	"endColumn": 96
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S1488",
	"severity": 4,
	"message": "Immediately return this expression instead of assigning it to the temporary variable \"s\".",
	"source": "sonarlint",
	"startLineNumber": 102,
	"startColumn": 24,
	"endLineNumber": 102,
	"endColumn": 71
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S6548",
	"severity": 4,
	"message": "A Singleton implementation was detected. Make sure the use of the Singleton pattern is required and the implementation is the right one for the context. [+1 location]",
	"source": "sonarlint",
	"startLineNumber": 107,
	"startColumn": 7,
	"endLineNumber": 107,
	"endColumn": 24
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S1488",
	"severity": 4,
	"message": "Immediately return this expression instead of assigning it to the temporary variable \"helloWorld\".",
	"source": "sonarlint",
	"startLineNumber": 113,
	"startColumn": 28,
	"endLineNumber": 113,
	"endColumn": 58
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S1488",
	"severity": 4,
	"message": "Immediately return this expression instead of assigning it to the temporary variable \"string\".",
	"source": "sonarlint",
	"startLineNumber": 120,
	"startColumn": 30,
	"endLineNumber": 120,
	"endColumn": 66
},{
	"resource": "/c:/Coding/SM Assiment1/Java/HelloWorld.java",
	"owner": "sonarlint",
	"code": "java:S1488",
	"severity": 4,
	"message": "Immediately return this expression instead of assigning it to the temporary variable \"code\".",
	"source": "sonarlint",
	"startLineNumber": 128,
	"startColumn": 22,
	"endLineNumber": 128,
	"endColumn": 45
}]


