const gulp = require('gulp'),
      browserSync = require('browser-sync').create(),
      sass = require('gulp-sass'),
      reload = browserSync.reload,
      sourceMaps = require('gulp-sourcemaps'),
      autoprefixer = require('gulp-autoprefixer'),
      coffee = require('gulp-coffee'),
      uglify = require('gulp-uglify'),
      minify = require('gulp-minify-css'),
      concat = require('gulp-concat')

const src = {
    sass: 'resources/assets/sass/**/*.scss',
    jsMixed: 'resources/assets/coffee/mixed/**/*.coffee',
    jsRaw: 'resources/assets/coffee/raw/**/*.coffee',
    img: 'resources/assets/img/**/*',
    libs: 'resources/vendor/**/*'
}

const dist = {
    css: 'static/css',
    js: 'static/js',
    img: 'static/img',
    libs: 'static/libs'
}

gulp.task('watch', ['sass-dev', 'scripts-raw-dev', 'scripts-mixed-dev', 'move'], function () {
    browserSync.init()
    gulp.watch(src.jsMixed, ['scripts-mixed-dev'])
    gulp.watch(src.jsRaw, ['scripts-raw-dev'])
    gulp.watch(src.sass, ['sass-dev'])
    gulp.watch([src.img, src.libs], ['move'])
})

gulp.task('sass', function () {
    return gulp.src(src.sass)
        .pipe(sass())
        .pipe(autoprefixer('last 2 versions'))
        .pipe(minify())
        .pipe(gulp.dest(dist.css))
})

gulp.task('sass-dev', function () {
    return gulp.src(src.sass)
        .pipe(sourceMaps.init())
        .pipe(sass())
        .pipe(autoprefixer('last 2 versions'))
        .pipe(minify())
        .pipe(sourceMaps.write())
        .pipe(gulp.dest(dist.css))
        .pipe(reload({stream: true}))
})

gulp.task('scripts-mixed', function () {
    return gulp.src(src.jsMixed)
        .pipe(coffee())
        .pipe(uglify())
        .pipe(concat('master.min.js'))
        .pipe(gulp.dest(dist.js))
})

gulp.task('scripts-mixed-dev', function () {
    return gulp.src(src.jsMixed)
        .pipe(sourceMaps.init())
        .pipe(coffee())
        .pipe(uglify())
        .pipe(concat('master.min.js'))
        .pipe(sourceMaps.write())
        .pipe(gulp.dest(dist.js))
})

gulp.task('scripts-raw', function () {
    return gulp.src(src.jsRaw)
        .pipe(coffee())
        .pipe(uglify())
        .pipe(gulp.dest(dist.js))
})

gulp.task('scripts-raw-dev', function () {
    return gulp.src(src.jsRaw)
        .pipe(sourceMaps.init())
        .pipe(coffee())
        .pipe(uglify())
        .pipe(sourceMaps.write())
        .pipe(gulp.dest(dist.js))
})

gulp.task('move', function () {
    gulp.src(src.libs).pipe(gulp.dest(dist.libs))
    gulp.src(src.img).pipe(gulp.dest(dist.img))
})

gulp.task('default', ['watch'])
gulp.task('build', ['sass', 'scripts-mixed', 'scripts-raw', 'move'])
