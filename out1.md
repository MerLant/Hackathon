```index.tsx
import { ColorModeScript } from "@chakra-ui/react";
import * as React from "react";
import * as ReactDOM from "react-dom/client";
import { App } from "./app/App";
import reportWebVitals from "./reportWebVitals";
import * as serviceWorker from "./serviceWorker";

const container = document.getElementById("root");
if (!container) throw new Error("Failed to find the root element");
const root = ReactDOM.createRoot(container);

root.render(
  <React.StrictMode>
    <ColorModeScript />
    <App />
  </React.StrictMode>,
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://cra.link/PWA
serviceWorker.unregister();

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

```

```serviceWorker.ts
// This optional code is used to register a service worker.
// register() is not called by default.

// This lets the app load faster on subsequent visits in production, and gives
// it offline capabilities. However, it also means that developers (and users)
// will only see deployed updates on subsequent visits to a page, after all the
// existing tabs open on the page have been closed, since previously cached
// resources are updated in the background.

// To learn more about the benefits of this model and instructions on how to
// opt-in, read https://cra.link/PWA

const isLocalhost = Boolean(
  window.location.hostname === "localhost" ||
    // [::1] is the IPv6 localhost address.
    window.location.hostname === "[::1]" ||
    // 127.0.0.0/8 are considered localhost for IPv4.
    window.location.hostname.match(
      /^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/,
    ),
)

type Config = {
  onSuccess?: (registration: ServiceWorkerRegistration) => void
  onUpdate?: (registration: ServiceWorkerRegistration) => void
}

export function register(config?: Config) {
  if (process.env.NODE_ENV === "production" && "serviceWorker" in navigator) {
    // The URL constructor is available in all browsers that support SW.
    const publicUrl = new URL(process.env.PUBLIC_URL, window.location.href)
    if (publicUrl.origin !== window.location.origin) {
      // Our service worker won't work if PUBLIC_URL is on a different origin
      // from what our page is served on. This might happen if a CDN is used to
      // serve assets; see https://github.com/facebook/create-react-app/issues/2374
      return
    }

    window.addEventListener("load", () => {
      const swUrl = `${process.env.PUBLIC_URL}/service-worker.js`

      if (isLocalhost) {
        // This is running on localhost. Let's check if a service worker still exists or not.
        checkValidServiceWorker(swUrl, config)

        // Add some additional logging to localhost, pointing developers to the
        // service worker/PWA documentation.
        navigator.serviceWorker.ready.then(() => {
          console.log(
            "This web app is being served cache-first by a service " +
              "worker. To learn more, visit https://cra.link/PWA",
          )
        })
      } else {
        // Is not localhost. Just register service worker
        registerValidSW(swUrl, config)
      }
    })
  }
}

function registerValidSW(swUrl: string, config?: Config) {
  navigator.serviceWorker
    .register(swUrl)
    .then((registration) => {
      registration.onupdatefound = () => {
        const installingWorker = registration.installing
        if (installingWorker == null) {
          return
        }
        installingWorker.onstatechange = () => {
          if (installingWorker.state === "installed") {
            if (navigator.serviceWorker.controller) {
              // At this point, the updated precached content has been fetched,
              // but the previous service worker will still serve the older
              // content until all client tabs are closed.
              console.log(
                "New content is available and will be used when all " +
                  "tabs for this page are closed. See https://cra.link/PWA.",
              )

              // Execute callback
              if (config && config.onUpdate) {
                config.onUpdate(registration)
              }
            } else {
              // At this point, everything has been precached.
              // It is the perfect time to display a
              // "Content is cached for offline use." message.
              console.log("Content is cached for offline use.")

              // Execute callback
              if (config && config.onSuccess) {
                config.onSuccess(registration)
              }
            }
          }
        }
      }
    })
    .catch((error) => {
      console.error("Error during service worker registration:", error)
    })
}

function checkValidServiceWorker(swUrl: string, config?: Config) {
  // Check if the service worker can be found. If it can't reload the page.
  fetch(swUrl, {
    headers: { "Service-Worker": "script" },
  })
    .then((response) => {
      // Ensure service worker exists, and that we really are getting a JS file.
      const contentType = response.headers.get("content-type")
      if (
        response.status === 404 ||
        (contentType != null && contentType.indexOf("javascript") === -1)
      ) {
        // No service worker found. Probably a different app. Reload the page.
        navigator.serviceWorker.ready.then((registration) => {
          registration.unregister().then(() => {
            window.location.reload()
          })
        })
      } else {
        // Service worker found. Proceed as normal.
        registerValidSW(swUrl, config)
      }
    })
    .catch(() => {
      console.log(
        "No internet connection found. App is running in offline mode.",
      )
    })
}

export function unregister() {
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.ready
      .then((registration) => {
        registration.unregister()
      })
      .catch((error) => {
        console.error(error.message)
      })
  }
}

```

```reportWebVitals.ts
import { ReportHandler } from "web-vitals"

const reportWebVitals = (onPerfEntry?: ReportHandler) => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import("web-vitals").then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry)
      getFID(onPerfEntry)
      getFCP(onPerfEntry)
      getLCP(onPerfEntry)
      getTTFB(onPerfEntry)
    })
  }
}

export default reportWebVitals

```

```react-app-env.d.ts
/// <reference types="node" />
/// <reference types="react" />
/// <reference types="react-dom" />

declare namespace NodeJS {
  interface ProcessEnv {
    readonly NODE_ENV: "development" | "production" | "test";
    readonly PUBLIC_URL: string;
  }
}

declare module "*.avif" {
  const src: string;
  export default src;
}

declare module "*.bmp" {
  const src: string;
  export default src;
}

declare module "*.gif" {
  const src: string;
  export default src;
}

declare module "*.jpg" {
  const src: string;
  export default src;
}

declare module "*.jpeg" {
  const src: string;
  export default src;
}

declare module "*.png" {
  const src: string;
  export default src;
}

declare module "*.webp" {
  const src: string;
  export default src;
}

declare module "*.svg" {
  import * as React from "react";

  export const ReactComponent: React.FunctionComponent<
    React.SVGProps<SVGSVGElement> & { title?: string }
  >;

  const src: string;
  export default src;
}

declare module "*.module.css" {
  const classes: { readonly [key: string]: string };
  export default classes;
}

declare module "*.module.scss" {
  const classes: { readonly [key: string]: string };
  export default classes;
}

declare module "*.module.sass" {
  const classes: { readonly [key: string]: string };
  export default classes;
}

```

```app/App.tsx
import React from "react";
import { ChakraProvider, theme } from "@chakra-ui/react";
import AppRouter from "./router";
import { Layout } from "src/shared/ui";

export const App = () => (
	<ChakraProvider theme={theme}>
		<Layout>
			<AppRouter />
		</Layout>
	</ChakraProvider>
);

```

```mock/localApiInstance.ts
import AxiosMockAdapter from "axios-mock-adapter";
import { Country } from "src/widgets/models/countries";
import { DetailedMovie } from "src/entities/models/Movie";

// ------------------ Начало блока генерации фильмов ------------------ //

const TOTAL_MOVIES = 50;

/** Генерируем случайное число в диапазоне [min, max] */
function randomInt(min: number, max: number) {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

/** Возвращает подмассив случайных элементов из массива arr (без повторений) */
function getRandomSubarray<T>(arr: T[], count: number): T[] {
	const shuffled = [...arr].sort(() => 0.5 - Math.random());
	return shuffled.slice(0, count);
}

/** Генерация случайных персон (актёров) */
function generateRandomPersons(count: number) {
	const persons = [];
	for (let i = 1; i <= count; i++) {
		persons.push({
			id: i,
			photo: "https://placehold.co/100x100",
			name: `Актёр №${i}`,
			enName: null,
			description: null,
			profession: "актёр",
			enProfession: "actor",
		});
	}
	return persons;
}

/**
 * Создаём базовый список фильмов (MovieBase),
 * а потом внизу «обогащаем» каждый фильм similarMovies и persons,
 * чтобы получился массив DetailedMovie
 */
const baseMovies = Array.from({ length: TOTAL_MOVIES }, (_, index) => {
	const id = index + 1;
	return {
		id,
		name: `Тестовый фильм №${id}`,
		year: randomInt(1950, 2025), // год от 1950 до 2025 (число)
		poster: {
			url: "https://placehold.co/300x500",
			previewUrl: "https://placehold.co/300x500",
		},
		rating: {
			kp: parseFloat((Math.random() * 10).toFixed(1)),
			imdb: parseFloat((Math.random() * 10).toFixed(1)),
			filmCritics: parseFloat((Math.random() * 10).toFixed(1)),
			russianFilmCritics: parseFloat((Math.random() * 10).toFixed(1)),
			await: parseFloat((Math.random() * 10).toFixed(1)),
		},
		ageRating: randomInt(0, 18),
		countries: [
			{
				name: id % 2 === 0 ? "США" : "Россия",
				slug: id % 2 === 0 ? "usa" : "russia",
			},
		],
		description: `Описание тестового фильма №${id}`,
	};
});

/**
 * Обогащаем каждый фильм:
 * - persons: случайный список актёров (3–7 человек)
 * - similarMovies: несколько случайных фильмов из общего списка (2–5 штук)
 */
export const allMovies: DetailedMovie[] = baseMovies.map((movie) => {
	// Подбираем «похожие фильмы»: 2–5 случайных других фильмов (исключаем сам фильм)
	const otherMovies = baseMovies.filter((m) => m.id !== movie.id);
	const randomSimilar = getRandomSubarray(otherMovies, randomInt(2, 5)).map(
		(m) => ({
			id: m.id,
			name: m.name,
			year: m.year,
			poster: m.poster,
			rating: m.rating,
		}),
	);

	// Генерируем 3–7 случайных актёров
	const randomActors = generateRandomPersons(randomInt(3, 7));

	return {
		...movie,
		persons: randomActors,
		similarMovies: randomSimilar,
	};
});

// ------------------ Конец блока генерации фильмов ------------------ //

// ------------------ Генерация отзывов ------------------ //

const TOTAL_REVIEWS = 100;

// Массив с «реальными» текстами отзывов
const reviewParagraphs = [
	"Этот фильм оставил незабываемые впечатления. Сюжет захватывающий, а визуальные эффекты на высшем уровне. Каждый кадр наполнен эмоциями и глубоким смыслом.",
	"Фильм поразил своей атмосферой и неожиданными поворотами. Актерская игра была убедительной, а саундтрек идеально дополнял происходящее на экране.",
	"Очень реалистичное повествование и яркие образы персонажей. Рекомендую к просмотру тем, кто ценит качественное кино и стремится к новым эмоциям.",
	"Режиссура и сценарий демонстрируют высокий уровень мастерства. Фильм заставляет задуматься над важными жизненными вопросами и вызывает целый спектр чувств.",
	"Эффектные визуальные решения и глубокая проработка персонажей делают этот фильм по-настоящему выдающимся. Он оставляет долгий послевкусие и желание пересмотреть его снова.",
];

// Функция, которая формирует длинный текст отзыва, выбирая 2-3 случайных абзаца
function generateLongReviewText(): string {
	const count = randomInt(2, 3);
	const paragraphs = getRandomSubarray(reviewParagraphs, count);
	return paragraphs.join(" ");
}

const allReviews = Array.from({ length: TOTAL_REVIEWS }, (_, index) => {
	const id = index + 1;
	// Назначаем случайный movieId от 1 до TOTAL_MOVIES
	const movieId = randomInt(1, TOTAL_MOVIES);
	return {
		id,
		movieId,
		title: `Отзыв о фильме №${movieId} - ${id}`,
		type: "review",
		review: generateLongReviewText(),
		date: new Date().toISOString(),
		author: `Автор ${randomInt(1, 10)}`,
		userRating: parseFloat((Math.random() * 10).toFixed(1)),
		authorId: randomInt(1, 10),
		createdAt: new Date().toISOString(),
		updatedAt: new Date().toISOString(),
	};
});

// ------------------ Инициализация моков ------------------ //

export function setupLocalApiMock(axiosInstance: any): void {
	const mock = new AxiosMockAdapter(axiosInstance);

	// 1) Мок для получения списка фильмов (с фильтрами)
	mock.onGet("/v1.4/movie").reply((config) => {
		const params = config.params || {};

		// Граничные значения фильтра
		const [yearFrom, yearTo] = (params.year || "1990-2025")
			.split("-")
			.map(Number);
		const [ratingFrom, ratingTo] = (params["rating.kp"] || "0-10")
			.split("-")
			.map(Number);
		const [ageFrom, ageTo] = (params.ageRating || "0-18")
			.split("-")
			.map(Number);

		const page = Number(params.page) || 1;
		const limit = Number(params.limit) || 20;
		const country = params.country || "Россия";

		const filtered = allMovies.filter((movie) => {
			const currentYear = movie.year ?? 0;
			const currentAgeRating = movie.ageRating ?? 0;
			const currentKpRating = movie.rating.kp ?? 0;

			const yearInRange =
				currentYear >= yearFrom && currentYear <= yearTo;
			const ageRatingInRange =
				currentAgeRating >= ageFrom && currentAgeRating <= ageTo;
			const ratingInRange =
				currentKpRating >= ratingFrom && currentKpRating <= ratingTo;

			const countryInRange = movie.countries.some(
				(c) => c.name === country,
			);

			return (
				yearInRange &&
				ageRatingInRange &&
				ratingInRange &&
				countryInRange
			);
		});

		const startIndex = (page - 1) * limit;
		const paginated = filtered.slice(startIndex, startIndex + limit);
		const pages = Math.ceil(filtered.length / limit);

		return [
			200,
			{
				docs: paginated,
				total: filtered.length,
				limit,
				page,
				pages,
			},
		];
	});

	// 2) Мок для получения детальной информации о фильме по ID
	mock.onGet(/\/v1\.4\/movie\/\d+$/).reply((config) => {
		const urlParts = config.url?.split("/") ?? [];
		const movieIdStr = urlParts[urlParts.length - 1];
		const movieId = Number(movieIdStr);

		const foundMovie = allMovies.find((m) => m.id === movieId);
		if (!foundMovie) {
			return [404, { message: "Movie not found" }];
		}

		return [200, foundMovie];
	});

	// 3) Мок для получения списка стран
	mock.onGet(
		/\/v1\/movie\/possible-values-by-field\?field=countries\.name/i,
	).reply(() => {
		const countries: Country[] = [
			{ name: "США", slug: "usa" },
			{ name: "Россия", slug: "russia" },
		];
		return [200, countries];
	});

	// 4) Мок для получения отзывов
	//    Ожидается, что запрос содержит параметры: page, limit, movieId (в виде строки, где ID разделены запятыми)
	mock.onGet("/v1.4/review").reply((config) => {
		const params = config.params || {};
		const page = Number(params.page) || 1;
		const limit = Number(params.limit) || 10;
		// Параметр movieId передается как строка, например "1,3,5"
		const movieIdsStr = params.movieId || "";
		const movieIds = movieIdsStr
			.split(",")
			.map((s: string) => Number(s))
			.filter((n: number) => !isNaN(n));

		// Фильтруем отзывы по заданным movieId
		const filteredReviews = allReviews.filter((review) =>
			movieIds.includes(review.movieId),
		);

		const startIndex = (page - 1) * limit;
		const paginatedReviews = filteredReviews.slice(
			startIndex,
			startIndex + limit,
		);
		const pages = Math.ceil(filteredReviews.length / limit);

		return [
			200,
			{
				docs: paginatedReviews,
				total: filteredReviews.length,
				limit,
				page,
				pages,
			},
		];
	});
}

```

```pages/index.ts
import MoviePage from "./movie";
import LandingPage from "./landing";
import NotFoundPage from "./notfound";

export { MoviePage, LandingPage, NotFoundPage };

```

```entities/ui/index.ts
import MovieCard from "./MovieCard/MovieCard";
import MovieFilter from "./MovieFilter/MovieFilter";
import Search from "./Search/Search";
import Pagination from "./Pagination/Pagination";
import PersonList from "./PersonaList/PersonaList";
import SimilarMovies from "./SimilarMovies/SimilarMovies";

export {
  MovieCard,
  MovieFilter,
  Search,
  Pagination,
  PersonList,
  SimilarMovies,
};

```

```entities/models/IMovieFilter.ts
export type Range = [number, number];

export interface FilterParams {
  yearRange: Range;
  ageRange: Range;
  ratingRange: Range;
  country?: string;
}

export interface FilterApplication {
  onApplyFilters: (filters: FilterParams) => void;
}

```

```entities/models/Movie.ts
import { Person } from "src/entities/models/IPersona";

export interface Country {
  name: string;
}

export interface MovieCardProps {
  movie: Movie;
}

export interface Movie extends MovieBase {
  ageRating: number | null;
  countries: Country[];
  description: string | null;
}

export interface MovieBase {
  id: number;
  name: string | null;
  year: number | null;
  poster: {
    url: string | null;
    previewUrl: string | null;
  };
  rating: {
    kp: number | null;
    imdb: number | null;
    filmCritics: number | null;
    russianFilmCritics: number | null;
    await: number | null;
  };
}

export interface DetailedMovie extends MovieBase {
  persons: Person[];
  similarMovies: MovieBase[];
  ageRating: number | null;
  countries: Country[];
  description: string | null;
}

```

```entities/models/ISearch.ts
export interface SearchMoviesParams {
  page?: number;
  limit?: number;
  query: string;
}

```

```entities/models/poster.ts
export interface Poster {
  previewUrl: string;
  id: string;
}

```

```entities/models/IPersona.ts
export interface PersonListProps {
  persons: Person[];
}

export interface Person {
  id: number;
  photo: string | null;
  name: string | null;
  enName: string | null;
  description: string | null;
  profession: string | null;
  enProfession: string | null;
}

```

```entities/api/search.ts
import { AxiosRequestConfig } from "axios";
import { createEffect } from "effector";
import { apiInstance } from "src/shared/api/base";
import { GetMoviesResponse } from "src/widgets/models/MovieModels";
import { SearchMoviesParams } from "../models/ISearch";

export const searchMoviesFx = createEffect<SearchMoviesParams, any>(
  async (params) => {
    const { page = 1, limit = 10, query } = params;
    const config: AxiosRequestConfig = {
      params: {
        page,
        limit,
        query,
      },
    };

    try {
      const response = await apiInstance.get<GetMoviesResponse>(
        `/v1.4/movie/search`,
        config,
      );
      return response;
    } catch (error) {
      console.error("Error during fetching movies:", error);
      throw error;
    }
  },
);

searchMoviesFx.fail.watch(({ error }) => {
  console.error("Failed to fetch movies with search:", error);
});

```

```entities/api/countries.ts
import { createEffect } from "effector";
import { apiInstance } from "src/shared/api/base";
import { Country } from "src/widgets/models/countries";

export const getCountriesFx = createEffect(async () => {
  const response = await apiInstance.get<Country[]>(
    "/v1/movie/possible-values-by-field?field=countries.name",
  );
  return response;
});

getCountriesFx.fail.watch(({ error }) => {
  console.error("Failed to fetch countries", error);
});

```

```entities/store/search.ts
import { createStore } from "effector";
import { searchMoviesFx } from "src/entities/api/search";
import { GetMoviesResponse } from "src/widgets/models/MovieModels";

const initialMoviesState: GetMoviesResponse = {
  docs: [],
  total: 0,
  limit: 10,
  page: 1,
  pages: 0,
};

const $searchStore = createStore<GetMoviesResponse>(initialMoviesState)
  .on(searchMoviesFx.doneData, (_, response) => {
    return response || initialMoviesState;
  })
  .on(searchMoviesFx.fail, (state, error) => {
    console.error("Failed to fetch movies:", error);
    return initialMoviesState;
  });

export { $searchStore };

```

```entities/store/countries.ts
import { createStore } from "effector";
import { getCountriesFx } from "src/entities/api/countries";
import { Country } from "src/widgets/models/countries";

const initialCountriesState: Country[] = [];

const $countriesStore = createStore<Country[]>(initialCountriesState)
  .on(getCountriesFx.doneData, (_, response) => {
    return response || [];
  })
  .on(getCountriesFx.fail, (state, error) => {
    console.error("Failed to fetch countries:", error);
    return [];
  });

export { $countriesStore };

```

```entities/ui/Pagination/Pagination.tsx
import React from "react";
import { HStack, Button, Text } from "@chakra-ui/react";
import {
  ArrowLeftIcon,
  ArrowBackIcon,
  ArrowForwardIcon,
  ArrowRightIcon,
} from "@chakra-ui/icons";

interface PaginationProps {
  page: number;
  maxPage: number;
  setPage: (page: number) => void;
}

const Pagination: React.FC<PaginationProps> = ({ page, maxPage, setPage }) => {
  return (
    <HStack my="5" justifyContent="center">
      <Button onClick={() => setPage(1)} isDisabled={page <= 1}>
        <ArrowLeftIcon />
      </Button>
      <Button onClick={() => setPage(page - 1)} isDisabled={page <= 1}>
        <ArrowBackIcon />
      </Button>
      <Text>
        {page} из {maxPage}
      </Text>
      <Button onClick={() => setPage(page + 1)} isDisabled={maxPage <= page}>
        <ArrowForwardIcon />
      </Button>
      <Button onClick={() => setPage(maxPage)} isDisabled={maxPage <= page}>
        <ArrowRightIcon />
      </Button>
    </HStack>
  );
};

export default Pagination;

```

```entities/ui/SimilarMovies/SimilarMovies.tsx
import React, { useState } from "react";
import {
  Box,
  Image,
  Link,
  Text,
  VStack,
  SimpleGrid,
  Center,
  Heading,
} from "@chakra-ui/react";
import { NavLink } from "react-router-dom";
import { MovieBase } from "../../models/Movie";
import { Pagination } from "src/entities/ui";
import { PATHS } from "src/app/router/paths";

interface SimilarMoviesProps {
  movies: MovieBase[];
}

const SimilarMovies: React.FC<SimilarMoviesProps> = ({ movies }) => {
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 3;
  const maxPage = Math.ceil(movies.length / itemsPerPage);

  const currentMovies = movies.slice(
    (currentPage - 1) * itemsPerPage,
    currentPage * itemsPerPage,
  );

  return (
    <Box>
      {movies.length > 0 ? (
        <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} spacing={5}>
          {currentMovies.map((movie) => (
            <Link as={NavLink} to={PATHS.FILM + "/" + movie.id} key={movie.id}>
              <VStack key={movie.id} spacing={3}>
                <Image
                  h="200"
                  borderRadius="10"
                  src={movie.poster.previewUrl || ""}
                  alt={movie.name || "Фильм"}
                />
                <Text>{movie.name}</Text>
              </VStack>
            </Link>
          ))}
        </SimpleGrid>
      ) : (
        <Heading>Похожие фильмы отсутствуют.</Heading>
      )}
      {maxPage > 1 && (
        <Center mt="8">
          <Pagination
            page={currentPage}
            maxPage={maxPage}
            setPage={setCurrentPage}
          />
        </Center>
      )}
    </Box>
  );
};

export default SimilarMovies;

```

```entities/ui/MovieCard/MovieCard.tsx
import {
  Card,
  Heading,
  HStack,
  Image,
  VStack,
  Text,
  Collapse,
  Button,
  Box,
  Center,
  Flex,
  Tag,
  Divider,
  LinkBox,
  LinkOverlay,
} from "@chakra-ui/react";
import { ViewOffIcon } from "@chakra-ui/icons";
import { useState } from "react";
import { MovieCardProps } from "src/entities/models/Movie";
import { CircleRating } from "src/shared/ui";
import { NavLink } from "react-router-dom";
import { PATHS } from "src/app/router/paths";

const MovieCard = ({ movie }: MovieCardProps) => {
  const [show, setShow] = useState(false);

  const handleToggle = () => setShow(!show);
  return (
    <LinkBox w="100%">
      <Card w="100%" p="2" borderRadius="25">
        <Flex direction={{ base: "column", md: "row" }} align="center">
          <Box flexShrink={0}>
            {movie.poster.previewUrl ? (
              <Image
                h="350"
                src={movie.poster.previewUrl}
                alt={`Постер ${movie.name}`}
                borderRadius="20"
              />
            ) : (
              <Card h="250px" w="100%" background="">
                <Center h="100%" w="100%">
                  <VStack>
                    <ViewOffIcon />
                    <Text>Постер отсутствует</Text>
                  </VStack>
                </Center>
              </Card>
            )}
          </Box>

          <Box flex="1" p="4">
            <VStack align="left" h="100%" justify="space-between">
              <LinkOverlay as={NavLink} to={PATHS.FILM + "/" + movie.id}>
                <HStack>
                  <Heading size="md">{movie.name}</Heading>
                  <Tag>+{movie.ageRating}</Tag>
                </HStack>
              </LinkOverlay>

              <Flex wrap="wrap" justifyContent="space-evenly">
                <CircleRating rating={movie.rating.kp}>Кинопоиск</CircleRating>
                <CircleRating rating={movie.rating.imdb}>IMDB</CircleRating>
                <CircleRating rating={movie.rating.filmCritics}>
                  Кинокритики
                </CircleRating>
                <CircleRating rating={movie.rating.filmCritics}>
                  Рус. критики
                </CircleRating>
              </Flex>
              <Divider />
              <HStack>
                <Tag>Год выхода:</Tag>
                <Text>{movie.year || "-"}</Text>
              </HStack>
              <Divider />
              <HStack>
                <Tag>Страна:</Tag>
                <Text>
                  {movie.countries.map((country) => country.name).join(", ") ||
                    "-"}
                </Text>
              </HStack>
              <Divider />
              <>
                <Collapse startingHeight={40} in={show}>
                  <Tag>Описание:</Tag> {movie.description || "-"}
                </Collapse>
                {movie.description && (
                  <Button size="sm" onClick={handleToggle} mt="1rem">
                    Показать {show ? "меньше" : "больше"}
                  </Button>
                )}
              </>
            </VStack>
          </Box>
        </Flex>
      </Card>
    </LinkBox>
  );
};

export default MovieCard;

```

```entities/ui/Search/Search.tsx
import React, { useState, useEffect } from "react";
import { useDebounce } from "src/shared/hooks/useDebounce";
import { searchMoviesFx } from "src/entities/api/search";
import { useUnit } from "effector-react";
import { $searchStore } from "src/entities/store/search";
import {
  Menu,
  MenuList,
  MenuItem,
  Input,
  Box,
  MenuButton,
  IconButton,
} from "@chakra-ui/react";
import { NavLink } from "react-router-dom";
import { PATHS } from "src/app/router/paths";

const Search = () => {
  const [input, setInput] = useState("");
  const debouncedSearchTerm = useDebounce(input, 1000);
  const movies = useUnit($searchStore);

  useEffect(() => {
    if (debouncedSearchTerm) {
      searchMoviesFx({ query: debouncedSearchTerm });
    }
  }, [debouncedSearchTerm]);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInput(event.target.value);
  };

  return (
    <Box width="150px" h="40px">
      <Menu isOpen={input.length > 0}>
        <Input
          variant="filled"
          type="text"
          value={input}
          onChange={handleChange}
          placeholder="Поиск..."
          width="100%"
        />
        <MenuButton
          as={IconButton}
          aria-label="Options"
          variant="outline"
          width="100%"
          h="0"
          border="0"
          m="0"
          p="0"
        ></MenuButton>
        <MenuList w="100%" p="0">
          {movies.docs
            .filter((movie) => movie.name)
            .map((movie) => (
              <MenuItem
                w="100%"
                key={movie.id}
                as={NavLink}
                onClick={() => {
                  setInput("");
                  movies.docs = [];
                }}
                to={PATHS.FILM + "/" + movie.id}
              >
                {movie.name}
              </MenuItem>
            ))}
        </MenuList>
      </Menu>
    </Box>
  );
};

export default Search;

```

```entities/ui/MovieFilter/MovieFilter.tsx
import {
  Drawer,
  DrawerBody,
  DrawerHeader,
  DrawerOverlay,
  DrawerContent,
  Button,
  useDisclosure,
  FormControl,
  FormLabel,
  RangeSlider,
  RangeSliderTrack,
  RangeSliderFilledTrack,
  RangeSliderThumb,
  Select,
  NumberInput,
  NumberInputField,
  HStack,
} from "@chakra-ui/react";
import { useState, useEffect } from "react";
import { useUnit } from "effector-react";
import { $countriesStore } from "src/entities/store/countries";
import {
  FilterApplication,
  FilterParams,
} from "src/entities/models/IMovieFilter";
import { getCountriesFx } from "src/entities/api/countries";

const safeParseInt = (value: string, fallback: number) => {
  const parsed = parseInt(value);
  return isNaN(parsed) ? fallback : parsed;
};

const MovieFilter: React.FC<
  FilterApplication & { initialFilters: FilterParams }
> = ({ onApplyFilters, initialFilters }) => {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [yearRange, setYearRange] = useState<[number, number]>(
    initialFilters.yearRange,
  );
  const [ageRange, setAgeRange] = useState<[number, number]>(
    initialFilters.ageRange,
  );
  const [ratingRange, setRatingRange] = useState<[number, number]>(
    initialFilters.ratingRange,
  );
  const [selectedCountry, setSelectedCountry] = useState<string>(
    initialFilters.country || "",
  );
  const countries = useUnit($countriesStore);
  const isPending = useUnit(getCountriesFx.pending);

  useEffect(() => {
    if (countries.length === 0 && !isPending) {
      getCountriesFx();
    }
  }, [countries, isPending]);

  const handleApplyFilters = () => {
    onApplyFilters({
      yearRange,
      ageRange,
      ratingRange,
      country: selectedCountry,
    });
    onClose();
  };

  return (
    <>
      <Button onClick={onOpen}>Фильтры</Button>
      <Drawer isOpen={isOpen} placement="right" onClose={onClose}>
        <DrawerOverlay />
        <DrawerContent>
          <DrawerHeader>Фильтр фильмов</DrawerHeader>
          <DrawerBody>
            <FormControl>
              <FormLabel>Года выхода</FormLabel>
              <HStack spacing={2}>
                <NumberInput
                  value={yearRange[0]}
                  max={yearRange[1]}
                  onChange={(valueString) =>
                    setYearRange([
                      safeParseInt(valueString, yearRange[0]),
                      yearRange[1],
                    ])
                  }
                >
                  <NumberInputField />
                </NumberInput>
                <NumberInput
                  value={yearRange[1]}
                  min={yearRange[0]}
                  onChange={(valueString) =>
                    setYearRange([
                      yearRange[0],
                      safeParseInt(valueString, yearRange[1]),
                    ])
                  }
                >
                  <NumberInputField />
                </NumberInput>
              </HStack>
              <RangeSlider
                min={1900}
                max={new Date().getFullYear()}
                value={yearRange}
                onChange={(val) => setYearRange(val as [number, number])}
                step={1}
              >
                <RangeSliderTrack>
                  <RangeSliderFilledTrack />
                </RangeSliderTrack>
                <RangeSliderThumb index={0} />
                <RangeSliderThumb index={1} />
              </RangeSlider>
            </FormControl>
            <FormControl mt="4">
              <FormLabel>Возростной рейтинг</FormLabel>
              <HStack spacing={2}>
                <NumberInput
                  value={ageRange[0]}
                  max={ageRange[1]}
                  onChange={(valueString) =>
                    setAgeRange([
                      safeParseInt(valueString, ageRange[0]),
                      ageRange[1],
                    ])
                  }
                >
                  <NumberInputField />
                </NumberInput>
                <NumberInput
                  value={ageRange[1]}
                  min={ageRange[0]}
                  onChange={(valueString) =>
                    setAgeRange([
                      ageRange[0],
                      safeParseInt(valueString, ageRange[1]),
                    ])
                  }
                >
                  <NumberInputField />
                </NumberInput>
              </HStack>
              <RangeSlider
                min={0}
                max={18}
                value={ageRange}
                onChange={(val) => setAgeRange(val as [number, number])}
                step={1}
              >
                <RangeSliderTrack>
                  <RangeSliderFilledTrack />
                </RangeSliderTrack>
                <RangeSliderThumb index={0} />
                <RangeSliderThumb index={1} />
              </RangeSlider>
            </FormControl>
            <FormControl mt="4">
              <FormLabel>Рейтинг фильма</FormLabel>
              <HStack spacing={2}>
                <NumberInput
                  value={ratingRange[0]}
                  max={ratingRange[1]}
                  onChange={(valueString) =>
                    setRatingRange([
                      safeParseInt(valueString, ratingRange[0]),
                      ratingRange[1],
                    ])
                  }
                >
                  <NumberInputField />
                </NumberInput>
                <NumberInput
                  value={ratingRange[1]}
                  min={ratingRange[0]}
                  onChange={(valueString) =>
                    setRatingRange([
                      ratingRange[0],
                      safeParseInt(valueString, ratingRange[1]),
                    ])
                  }
                >
                  <NumberInputField />
                </NumberInput>
              </HStack>
              <RangeSlider
                min={0}
                max={10}
                value={ratingRange}
                onChange={(val) => setRatingRange(val as [number, number])}
                step={0.1}
              >
                <RangeSliderTrack>
                  <RangeSliderFilledTrack />
                </RangeSliderTrack>
                <RangeSliderThumb index={0} />
                <RangeSliderThumb index={1} />
              </RangeSlider>
            </FormControl>
            <FormControl mt="4">
              <FormLabel>Страна</FormLabel>
              <Select
                placeholder="Выберите страну"
                value={selectedCountry}
                onChange={(e) => setSelectedCountry(e.target.value)}
              >
                {countries.map((country) => (
                  <option key={country.name} value={country.name}>
                    {country.name}
                  </option>
                ))}
              </Select>
            </FormControl>
            <Button mt="4" colorScheme="blue" onClick={handleApplyFilters}>
              Применить фильтры
            </Button>
          </DrawerBody>
        </DrawerContent>
      </Drawer>
    </>
  );
};

export default MovieFilter;

```

```entities/ui/PersonaList/PersonaList.tsx
import React, { useState } from "react";
import {
  Box,
  Avatar,
  Text,
  VStack,
  SimpleGrid,
  Center,
  Card,
  useBreakpointValue,
} from "@chakra-ui/react";
import { PersonListProps } from "../../models/IPersona";
import { Pagination } from "src/entities/ui";

const PersonList: React.FC<PersonListProps> = ({ persons }) => {
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 5;
  const maxPage = Math.ceil(persons.length / itemsPerPage);

  const currentPersons = persons.slice(
    (currentPage - 1) * itemsPerPage,
    currentPage * itemsPerPage,
  );

  const columns = useBreakpointValue({ base: 1, md: 5 });

  return (
    <Box>
      <SimpleGrid columns={columns} spacing={5}>
        {currentPersons.map((person) => (
          <Card h="200" key={person.id}>
            <VStack
              justifyContent="space-between"
              key={person.id}
              p={4}
              borderRadius="lg"
              h="100%"
            >
              <Avatar
                src={person.photo || ""}
                size="lg"
                name={person.name || "Имя отсутствует"}
              />
              <Text fontWeight="bold">{person.name || "Имя отсутствует"}</Text>
              <Text fontSize="sm">
                {person.profession || "Профессия отсутствует"}
              </Text>
            </VStack>
          </Card>
        ))}
      </SimpleGrid>
      {maxPage > 1 && (
        <Center mt="8">
          <Pagination
            page={currentPage}
            maxPage={maxPage}
            setPage={setCurrentPage}
          />
        </Center>
      )}
    </Box>
  );
};

export default PersonList;

```

```widgets/ui/index.ts
import MovieBlock from "./MovieBlock/MovieBlock";
import Header from "./Header/Header";
import MovieInfo from "./MovieInfo/MovieInfo";

export { MovieBlock, Header, MovieInfo };

```

```widgets/models/MovieModels.ts
import { Movie } from "src/entities/models/Movie";

export interface GetMoviesResponse {
  docs: Movie[];
  total: number;
  limit: number;
  page: number;
  pages: number;
}

```

```widgets/models/countries.ts
export interface Country {
  name: string;
  slug: string;
}

```

```widgets/api/movie.ts
import axios, { AxiosRequestConfig } from "axios";
import { createEffect } from "effector";
import { GetMoviesResponse } from "src/widgets/models/MovieModels";
import { apiInstance } from "src/shared/api/base";

type GetMoviesFxParams = {
  page?: number;
  limit?: number;
  sortField?: string[];
  sortType?: string[];
  year?: string[];
  ratingKp?: string[];
  ageRating?: string[];
  countriesName?: string[];
  selectFields?: string[];
};

export const getMoviesFx = createEffect<GetMoviesFxParams, GetMoviesResponse>(
  async ({
    page = 1,
    limit = 10,
    year = [],
    ratingKp = [],
    ageRating = [],
    countriesName = [],
    selectFields = [
      "id",
      "name",
      "description",
      "year",
      "rating",
      "ageRating",
      "countries",
      "poster",
    ],
  } = {}) => {
    const cancelTokenSource = axios.CancelToken.source();
    const fields = selectFields.join("&selectFields=");
    const options: AxiosRequestConfig = {
      cancelToken: cancelTokenSource.token,
      params: {
        page,
        limit,
        selectFields: fields,
      },
      paramsSerializer: (params) => {
        return Object.keys(params)
          .map((key) => `${key}=${params[key]}`)
          .join("&");
      },
    };

    if (year.length > 0) {
      options.params.year = year.join(",");
    }
    if (ratingKp.length > 0) {
      options.params["rating.kp"] = ratingKp.join(",");
    }
    if (ageRating.length > 0) {
      options.params.ageRating = ageRating.join(",");
    }
    if (countriesName.length > 0 && countriesName[0] !== "") {
      options.params["countries.name"] = countriesName.join(",");
    }

    const response = await apiInstance.get<GetMoviesResponse>(
      `/v1.4/movie`,
      options,
    );

    return response;
  },
);

```

```widgets/store/movie.ts
import { createStore } from "effector";
import { getMoviesFx } from "src/widgets/api/movie";
import { GetMoviesResponse } from "src/widgets/models/MovieModels";

const initialMoviesState: GetMoviesResponse = {
  docs: [],
  total: 0,
  limit: 10,
  page: 1,
  pages: 0,
};

const $moviesStore = createStore(initialMoviesState)
  .on(getMoviesFx.doneData, (state, response) => {
    return response;
  })
  .on(getMoviesFx.fail, (state, error) => {
    console.error("Failed to fetch movies:", error);
    return {
      ...state,
      docs: [],
    };
  });

export { $moviesStore };

```

```widgets/ui/MovieBlock/MovieBlock.tsx
import {
  Box,
  FormControl,
  FormLabel,
  Heading,
  HStack,
  Select,
} from "@chakra-ui/react";
import { useUnit } from "effector-react";
import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { MovieList } from "src/features/ui";
import { MovieFilter, Pagination } from "src/entities/ui";
import { getMoviesFx } from "src/widgets/api/movie";
import { FilterParams } from "src/entities/models/IMovieFilter";
import { $moviesStore } from "src/widgets/store/movie";

const MovieBlock = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const movies = useUnit($moviesStore);

  const [page, setPage] = useState(
    parseInt(new URLSearchParams(location.search).get("page") || "1", 10),
  );
  const [limit, setLimit] = useState(
    parseInt(new URLSearchParams(location.search).get("limit") || "10", 10),
  );
  const [filters, setFilters] = useState<FilterParams>({
    yearRange: [
      parseInt(
        new URLSearchParams(location.search).get("yearFrom") || "1990",
        10,
      ),
      parseInt(
        new URLSearchParams(location.search).get("yearTo") ||
          `${new Date().getFullYear()}`,
        10,
      ),
    ],
    ageRange: [
      parseInt(new URLSearchParams(location.search).get("ageFrom") || "0", 10),
      parseInt(new URLSearchParams(location.search).get("ageTo") || "18", 10),
    ],
    ratingRange: [
      parseInt(
        new URLSearchParams(location.search).get("ratingFrom") || "0",
        10,
      ),
      parseInt(
        new URLSearchParams(location.search).get("ratingTo") || "10",
        10,
      ),
    ],
    country: new URLSearchParams(location.search).get("country") || "",
  });

  useEffect(() => {
    const params = new URLSearchParams();
    params.set("page", page.toString());
    params.set("limit", limit.toString());
    params.set("yearFrom", filters.yearRange[0].toString());
    params.set("yearTo", filters.yearRange[1].toString());
    params.set("ageFrom", filters.ageRange[0].toString());
    params.set("ageTo", filters.ageRange[1].toString());
    params.set("ratingFrom", filters.ratingRange[0].toString());
    params.set("ratingTo", filters.ratingRange[1].toString());
    if (filters.country) {
      params.set("country", filters.country);
    }

    navigate(`?${params.toString()}`, { replace: true });

    getMoviesFx({
      page,
      limit,
      year: [`${filters.yearRange[0]}-${filters.yearRange[1]}`],
      ageRating: [`${filters.ageRange[0]}-${filters.ageRange[1]}`],
      ratingKp: [`${filters.ratingRange[0]}-${filters.ratingRange[1]}`],
      countriesName: [`${filters.country}`],
    });
  }, [filters, page, limit, navigate]);

  const handleApplyFilters = (newFilters: FilterParams) => {
    setFilters(newFilters);
  };

  return (
    <Box>
      <HStack justifyContent="space-between">
        <Heading mb="4">Фильмы и сериалы</Heading>
        <MovieFilter
          onApplyFilters={handleApplyFilters}
          initialFilters={filters}
        />
      </HStack>
      <Pagination page={page} maxPage={movies.pages} setPage={setPage} />

      <MovieList movieList={movies.docs} />
      <Pagination page={page} maxPage={movies.pages} setPage={setPage} />
      <FormControl mt="5">
        <FormLabel>Количество на странице</FormLabel>
        <Select
          value={limit}
          onChange={(e) => setLimit(parseInt(e.target.value, 10))}
        >
          <option value="5">5</option>
          <option value="10">10</option>
          <option value="20">20</option>
          <option value="50">50</option>
        </Select>
      </FormControl>
    </Box>
  );
};

export default MovieBlock;

```

```widgets/ui/Header/Header.tsx
import {
  Box,
  Button,
  ButtonGroup,
  Flex,
  Heading,
  Spacer,
  useColorModeValue,
} from "@chakra-ui/react";
import { NavLink } from "react-router-dom";
import { PATHS } from "src/app/router/paths";
import { Search } from "src/entities/ui";
import { ColorModeSwitcher } from "src/features/ui";

const Header = () => {
  const bgColor = useColorModeValue("gray.200", "gray.700");
  return (
    <header>
      <Flex
        minWidth="max-content"
        alignItems="center"
        gap="2"
        marginY="8px"
        marginX="4%"
        borderRadius="lg"
        padding="4px"
        bg={bgColor}
      >
        <Box p="2" gap="2">
          <Button as={NavLink} to={PATHS.HOME} _hover={{}}>
            <Heading
              display={"inline"}
              size="md"
              bgGradient="linear(to-l, #7928CA, #FF0080)"
              bgClip="text"
            >
              К
            </Heading>
          </Button>
        </Box>

        <Spacer />
        <Search />

        <Spacer />
        <ButtonGroup gap="2">
          <ColorModeSwitcher />
        </ButtonGroup>
      </Flex>
    </header>
  );
};

export default Header;

```

```widgets/ui/MovieInfo/MovieInfo.tsx
import { VStack } from "@chakra-ui/react";
import {
  MovieDetails,
  MovieReviews,
  MovieSeason,
  PosterList,
} from "src/features/ui";

interface MovieInfoProps {
  movieId: number;
}

const MovieInfo = ({ movieId }: MovieInfoProps) => {
  return (
    <>
      <VStack>
        <MovieDetails movieId={movieId} />
        <PosterList movieId={movieId} />
        <MovieSeason movieId={movieId} />
        <MovieReviews movieId={movieId} />
      </VStack>
    </>
  );
};

export default MovieInfo;

```

```pages/landing/index.ts
import LandingPage from "./ui/LandingPage";

export default LandingPage;

```

```pages/movie/index.ts
import MoviePage from "./ui/MoviePage";

export default MoviePage;

```

```pages/notfound/index.ts
import NotFoundPage from "./ui/NotFoundPage";

export default NotFoundPage;

```

```pages/notfound/ui/NotFoundPage.tsx
import { PATHS } from "src/app/router/paths";
import { Button, Center, Heading, HStack, Stack } from "@chakra-ui/react";
import { NavLink } from "react-router-dom";
import { BackButton } from "src/shared/ui";

const NotFoundPage = () => {
  return (
    <Center marginY="8px" marginX="4%" padding="4px" minH="100%">
      <Stack spacing={4}>
        <Heading>Страница не найдена!</Heading>
        <HStack>
          <BackButton step={3} />
          <Button as={NavLink} to={PATHS.HOME}>
            Вернуться на главную
          </Button>
        </HStack>
      </Stack>
    </Center>
  );
};

export default NotFoundPage;

```

```pages/movie/ui/MoviePage.tsx
import { Box } from "@chakra-ui/react";
import { BackButton } from "src/shared/ui";
import { MovieInfo } from "src/widgets/ui";
import { useNavigate, useParams } from "react-router-dom";
import { PATHS } from "src/app/router/paths";
import { useEffect } from "react";

const MoviePage = () => {
  const navigate = useNavigate();
  const { movieId } = useParams();

  useEffect(() => {
    if (!movieId || isNaN(Number(movieId))) {
      navigate(PATHS.NOTFOUND);
    }
  }, [movieId, navigate]);

  if (!movieId || isNaN(Number(movieId))) {
    return null;
  }

  return (
    <Box marginY="8px" marginX="4%" padding="4px">
      <BackButton />
      <MovieInfo movieId={+movieId} />
    </Box>
  );
};

export default MoviePage;

```

```pages/landing/ui/LandingPage.tsx
import { Box } from "@chakra-ui/react";
import { MovieBlock } from "src/widgets/ui";

const LandingPage = () => {
  return (
    <Box marginY="8px" marginX="4%" padding="4px">
      <MovieBlock />
    </Box>
  );
};

export default LandingPage;

```

```shared/ui/index.ts
import Layout from "./Layout/Layout";
import CircleRating from "./CircleRating/CircleRating";
import BackButton from "./BackButton/BackButton";

export { Layout, CircleRating, BackButton };

```

```shared/models/ICircleRating.tsx
export interface CircleRatingProps {
  rating: number | null;
  children: React.ReactNode;
}

```

```shared/models/LayoutModels.ts
import { ReactNode } from "react";

export interface ILayout {
  children: ReactNode;
}

```

```shared/hooks/useDebounce.ts
import { useState, useEffect } from "react";

export function useDebounce<T>(value: T, delay: number) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
}

```

```shared/api/base.ts
import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from "axios";
import { setupLocalApiMock } from "src/mock/localApiInstance";

const USE_MOCK = true; // process.env.USE_MOCK === "true";

export const API_URL = "https://api.kinopoisk.dev/";

class ApiInstance {
	private axios: AxiosInstance;

	constructor() {
		this.axios = axios.create({
			baseURL: API_URL,
			timeout: 120000,
			headers: {
				"Content-Type": "application/json",
				"X-API-KEY": process.env.TOKEN,
			},
		});

		// Подключаем локальный мок, если активирован режим MOCK
		if (USE_MOCK) {
			setupLocalApiMock(this.axios);
		}
	}

	async get<T>(
		endpoint: string,
		options: AxiosRequestConfig = {},
		retryCount: number = 3,
	): Promise<T> {
		let lastError: unknown;

		for (let attempt = 0; attempt < retryCount; attempt++) {
			try {
				const response: AxiosResponse<T> = await this.axios.get(
					endpoint,
					options,
				);
				return response.data;
			} catch (error) {
				lastError = error;
				console.error(`Attempt ${attempt + 1} failed: ${error}`);

				if (attempt < retryCount - 1) {
					await this.delay(1000);
				}
			}
		}

		throw lastError;
	}

	private delay(ms: number): Promise<void> {
		return new Promise((resolve) => setTimeout(resolve, ms));
	}
}

export const apiInstance = new ApiInstance();

```

```shared/ui/Layout/Layout.tsx
import { Box } from "@chakra-ui/react";
import { ILayout } from "src/shared/models/LayoutModels";

const Layout: React.FC<ILayout> = ({ children }) => {
  return <Box minH="100vh">{children}</Box>;
};

export default Layout;

```

```shared/ui/CircleRating/CircleRating.tsx
import {
  CircularProgress,
  CircularProgressLabel,
  Tag,
  useColorModeValue,
  VStack,
} from "@chakra-ui/react";
import { CircleRatingProps } from "src/shared/models/ICircleRating";

const getRatingColor = (rating: number) => {
  if (rating >= 8.5) {
    return "green.500";
  } else if (rating >= 7) {
    return "green.400";
  } else if (rating >= 6) {
    return "yellow.400";
  } else if (rating >= 5) {
    return "orange.400";
  } else if (rating >= 4) {
    return "red.400";
  } else if (rating >= 3) {
    return "red.600";
  } else if (rating > 0) {
    return "red.800";
  } else {
    return "gray.400";
  }
};

const CircleRating = ({ rating, children }: CircleRatingProps) => {
  const bgColor = useColorModeValue("gray.200", "gray.600");

  if (!rating) {
    return (
      <VStack mb="5px">
        <CircularProgress value={0} color="gray.400" trackColor={bgColor}>
          <CircularProgressLabel>-</CircularProgressLabel>
        </CircularProgress>
        <Tag>{children}</Tag>
      </VStack>
    );
  }
  const color = getRatingColor(rating);
  return (
    <VStack mb="5px">
      <CircularProgress value={rating * 10} color={color} trackColor={bgColor}>
        <CircularProgressLabel>
          {rating.toFixed(0)}/10 <br />
        </CircularProgressLabel>
      </CircularProgress>
      <Tag>{children}</Tag>
    </VStack>
  );
};

export default CircleRating;

```

```shared/ui/BackButton/BackButton.tsx
import { Button } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";

interface BackButtonProps {
  step?: number;
}

const BackButton = ({ step = 1 }: BackButtonProps) => {
  let navigate = useNavigate();

  function handleBack() {
    navigate(-step);
  }
  return (
    <Button mb="3" onClick={handleBack}>
      Назад
    </Button>
  );
};

export default BackButton;

```

```features/ui/index.ts
import ColorModeSwitcher from "./ColorModeSwitcher/ColorModeSwitcher";
import MovieList from "./MovieList/MovieList";
import MovieDetails from "./MovieDetails/MovieDetails";
import PosterList from "./PosterList/PosterList";
import MovieSeason from "./MovieSeason/MovieSeason";
import MovieReviews from "./MovieReview/MovieReview";

export {
  ColorModeSwitcher,
  MovieList,
  MovieDetails,
  PosterList,
  MovieSeason,
  MovieReviews,
};

```

```features/models/IMovieDetails.ts
export interface MovieDetailsProps {
  movieId: number;
}

```

```features/models/review.ts
export interface Review {
  id: number;
  movieId: number;
  title: string | null;
  type: string | null;
  review: string | null;
  date: string | null;
  author: string | null;
  userRating: number | null;
  authorId: number | null;
  createdAt: string | null;
  updatedAt: string | null;
}

export interface ReviewsResponse {
  docs: Review[];
  total: number;
  limit: number;
  page: number;
  pages: number;
}

export interface MovieReviewsProps {
  movieId: number;
}

```

```features/models/IPosterList.ts
import { Poster } from "src/entities/models/poster";

export interface PosterResponse {
  docs: Poster[];
  total: number;
  limit: number;
  page: number;
  pages: number;
}

export interface MoviePostersProps {
  movieId: number;
}

```

```features/models/IMovieSeasons.ts
export interface SeasonResponse {
  docs: Season[];
  total: number;
  limit: number;
  page: number;
  pages: number;
}

export interface Season {
  number: number;
  episodes: Episode[];
  name: string | null;
  poster: Image | null;
  id: string;
}

export interface Episode {
  number: number;
  name: string | null;
  enName: string | null;
  still: Image;
  duration: number | null;
  date: string | null;
  description: string | null;
  airDate: string | null;
  enDescription: string | null;
}

export interface Image {
  url: string | null;
  previewUrl: string | null;
}

export interface FetchSeasonsParams {
  page?: number;
  limit?: number;
  movieId: number[];
  selectFields?: string[];
}

```

```features/models/IMovieList.ts
import { Movie } from "src/entities/models/Movie";

export interface MovieListProps {
  movieList: Movie[];
}

```

```features/api/MovieDetails.ts
import { createEffect } from "effector";
import { apiInstance } from "src/shared/api/base";
import { DetailedMovie } from "src/entities/models/Movie";

export const getMovieDetailsFx = createEffect(async (movieId: number) => {
  const response = await apiInstance.get<DetailedMovie>(
    `/v1.4/movie/${movieId}`,
  );
  return response;
});

getMovieDetailsFx.fail.watch(({ error }) => {
  console.error("Failed to fetch movie details", error);
});

```

```features/api/poster.ts
import { createEffect } from "effector";
import { AxiosRequestConfig } from "axios";
import { apiInstance } from "src/shared/api/base";
import { PosterResponse } from "../models/IPosterList";

export const getMoviePostersFx = createEffect<
  { movieId: number[]; page: number; limit: number },
  PosterResponse
>(async ({ movieId, page = 1, limit = 10 }) => {
  const selectFields = ["previewUrl"];
  const config: AxiosRequestConfig = {
    params: {
      page,
      limit,
      selectFields: selectFields.join(","),
      movieId: movieId.join(","),
    },
    paramsSerializer: (params) => {
      return Object.keys(params)
        .map((key) => `${key}=${encodeURIComponent(params[key])}`)
        .join("&");
    },
  };

  try {
    const response = await apiInstance.get<PosterResponse>(
      "/v1.4/image",
      config,
    );
    return response;
  } catch (error) {
    console.error("Error during fetching movie posters:", error);
    throw error;
  }
});

getMoviePostersFx.fail.watch(({ error }) => {
  console.error("Failed to fetch movie posters", error);
});

```

```features/api/review.ts
import { createEffect } from "effector";
import { AxiosRequestConfig } from "axios";
import { apiInstance } from "src/shared/api/base";
import { ReviewsResponse } from "../models/review";

export const getReviewsFx = createEffect<
  { page: number; limit: number; movieId: string[] },
  ReviewsResponse
>(async ({ page = 1, limit = 10, movieId }) => {
  const config: AxiosRequestConfig = {
    params: {
      page,
      limit,
      movieId: movieId.join(","),
    },
    paramsSerializer: (params) => {
      return Object.keys(params)
        .map((key) => `${key}=${encodeURIComponent(params[key])}`)
        .join("&");
    },
  };

  try {
    const response = await apiInstance.get<ReviewsResponse>(
      "/v1.4/review",
      config,
    );
    return response;
  } catch (error) {
    console.error("Error during fetching reviews:", error);
    throw error;
  }
});

getReviewsFx.fail.watch(({ error }) => {
  console.error("Failed to fetch reviews", error);
});

```

```features/api/seasons.ts
import { createEffect } from "effector";
import { AxiosRequestConfig } from "axios";
import { apiInstance } from "src/shared/api/base";
import { SeasonResponse, FetchSeasonsParams } from "../models/IMovieSeasons";

export const getSeasonsFx = createEffect<FetchSeasonsParams, SeasonResponse>(
  async (params) => {
    const {
      page = 1,
      limit = 10,
      movieId,
      selectFields = ["poster", "number", "name", "episodes"],
    } = params;

    const config: AxiosRequestConfig = {
      params: {
        page,
        limit,
        movieId: movieId.join(","),
      },
      paramsSerializer: (params) => {
        const selectParams = selectFields
          .map((field) => `selectFields=${encodeURIComponent(field)}`)
          .join("&");
        const otherParams = Object.keys(params)
          .filter((key) => key !== "selectFields")
          .map((key) => `${key}=${encodeURIComponent(params[key])}`)
          .join("&");
        return `${selectParams}&${otherParams}`;
      },
    };

    try {
      const response = await apiInstance.get<SeasonResponse>(
        "/v1.4/season",
        config,
      );
      return response;
    } catch (error) {
      console.error("Error fetching seasons:", error);
      throw error;
    }
  },
);

getSeasonsFx.fail.watch(({ error }) => {
  console.error("Failed to fetch seasons", error);
});

```

```features/store/MovieDetails.ts
import { createStore } from "effector";
import { getMovieDetailsFx } from "../api/MovieDetails";
import { DetailedMovie } from "src/entities/models/Movie";

const initialMovieState: DetailedMovie = {
  id: 0,
  name: null,
  description: null,
  year: null,
  ageRating: null,
  poster: {
    url: null,
    previewUrl: null,
  },
  countries: [],
  rating: {
    kp: null,
    imdb: null,
    filmCritics: null,
    russianFilmCritics: null,
    await: null,
  },
  persons: [],
  similarMovies: [],
};

const $movieDetailsStore = createStore<DetailedMovie>(initialMovieState)
  .on(getMovieDetailsFx.doneData, (_, response) => {
    return response;
  })
  .on(getMovieDetailsFx.fail, (state, error) => {
    console.error("Failed to fetch movie details:", error);
    return initialMovieState;
  });

export { $movieDetailsStore };

```

```features/store/poster.ts
import { createStore } from "effector";
import { getMoviePostersFx } from "../api/poster";
import { PosterResponse } from "../models/IPosterList";

const initialPostersState: PosterResponse = {
  docs: [],
  total: 0,
  limit: 10,
  page: 1,
  pages: 1,
};

const $postersStore = createStore<PosterResponse>(initialPostersState)
  .on(getMoviePostersFx.doneData, (_, response) => {
    return response || initialPostersState;
  })
  .on(getMoviePostersFx.fail, (state, error) => {
    console.error("Failed to fetch movie posters:", error);
    return {
      ...state,
      docs: [],
    };
  });

export { $postersStore };

```

```features/store/review.ts
import { createStore } from "effector";
import { getReviewsFx } from "../api/review";
import { ReviewsResponse } from "../models/review";

const initialReviewState: ReviewsResponse = {
  docs: [],
  total: 0,
  limit: 10,
  page: 1,
  pages: 0,
};

const $reviewsStore = createStore<ReviewsResponse>(initialReviewState)
  .on(getReviewsFx.doneData, (_, response) => {
    return response;
  })
  .on(getReviewsFx.fail, (state, error) => {
    console.error("Failed to fetch reviews:", error);
    return state;
  });

export { $reviewsStore };

```

```features/store/seasons.ts
import { createStore } from "effector";
import { getSeasonsFx } from "../api/seasons";
import { SeasonResponse } from "../models/IMovieSeasons";

const initialSeasonsState: SeasonResponse = {
  docs: [],
  total: 0,
  limit: 10,
  page: 1,
  pages: 0,
};

const $seasonsStore = createStore<SeasonResponse>(initialSeasonsState)
  .on(getSeasonsFx.doneData, (_, response) => {
    return response || initialSeasonsState;
  })
  .on(getSeasonsFx.fail, (state, error) => {
    console.error("Failed to fetch seasons:", error);
    return state;
  });

export { $seasonsStore };

```

```features/ui/ColorModeSwitcher/ColorModeSwitcher.tsx
import React from "react";
import {
  useColorMode,
  useColorModeValue,
  IconButton,
  IconButtonProps,
} from "@chakra-ui/react";
import { FaMoon, FaSun } from "react-icons/fa";

type ColorModeSwitcherProps = Omit<IconButtonProps, "aria-label">;

const ColorModeSwitcher: React.FC<ColorModeSwitcherProps> = (props) => {
  const { toggleColorMode } = useColorMode();
  const text = useColorModeValue("dark", "light");
  const SwitchIcon = useColorModeValue(FaMoon, FaSun);

  return (
    <IconButton
      size="md"
      fontSize="lg"
      variant="ghost"
      color="current"
      marginLeft="2"
      onClick={toggleColorMode}
      icon={<SwitchIcon />}
      aria-label={`Switch to ${text} mode`}
      {...props}
    />
  );
};

export default ColorModeSwitcher;

```

```features/ui/MovieSeason/MovieSeason.tsx
import React, { useEffect, useState } from "react";
import { useUnit } from "effector-react";
import { $seasonsStore } from "../../store/seasons";
import { getSeasonsFx } from "../../api/seasons";
import { Box, Select, Image, Text, VStack, Heading } from "@chakra-ui/react";

interface MovieSeasonProps {
  movieId: number;
}

const MovieSeason = ({ movieId }: MovieSeasonProps) => {
  const seasons = useUnit($seasonsStore);
  const [selectedSeason, setSelectedSeason] = useState("");
  const [selectedEpisode, setSelectedEpisode] = useState("");

  useEffect(() => {
    getSeasonsFx({ movieId: [movieId] });
  }, [movieId]);

  const handleSeasonChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedSeason(event.target.value);
    setSelectedEpisode("");
  };

  const handleEpisodeChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedEpisode(event.target.value);
  };

  const selectedSeasonData = seasons.docs.find(
    (season) => season.id === selectedSeason,
  );
  const selectedEpisodeData = selectedSeasonData?.episodes.find(
    (episode) => episode.number.toString() === selectedEpisode,
  );

  if (seasons.total === 0) {
    return null;
  }

  return (
    <Box p={5}>
      <VStack spacing={4} align="stretch">
        <Select
          placeholder="Выберите сезон"
          onChange={handleSeasonChange}
          value={selectedSeason}
        >
          {seasons.docs.map((season) => (
            <option key={season.id} value={season.id}>
              {season.name}
            </option>
          ))}
        </Select>
        {selectedSeason && (
          <Select
            placeholder="Выберите эпизод"
            onChange={handleEpisodeChange}
            value={selectedEpisode}
          >
            {selectedSeasonData?.episodes.map((episode) => (
              <option key={episode.number} value={episode.number}>
                {episode.name || `Эпизод ${episode.number}`}
              </option>
            ))}
          </Select>
        )}
        {selectedEpisode && (
          <Box>
            <Heading size="md">
              {selectedEpisodeData?.name || "Нет названиея"}
            </Heading>
            {selectedEpisodeData?.still.url ? (
              <Image
                borderRadius="10"
                src={selectedEpisodeData.still.url}
                alt={selectedEpisodeData.name || "Нет постера"}
              />
            ) : (
              <Text>Нет постера </Text>
            )}
          </Box>
        )}
      </VStack>
    </Box>
  );
};

export default MovieSeason;

```

```features/ui/PosterList/PosterList.tsx
import React, { useEffect, useState } from "react";
import { Box, Image, SimpleGrid, Text, Center } from "@chakra-ui/react";
import { useUnit } from "effector-react";
import { getMoviePostersFx } from "../../api/poster";
import { $postersStore } from "../../store/poster";
import { Pagination } from "src/entities/ui";
import { MoviePostersProps } from "src/features/models/IPosterList";

const PosterList: React.FC<MoviePostersProps> = ({ movieId }) => {
  const posters = useUnit($postersStore);
  const [page, setPage] = useState(1);

  useEffect(() => {
    getMoviePostersFx({ movieId: [movieId], page, limit: 3 });
  }, [movieId, page]);

  if (posters.docs.length === 0 && !posters.total) {
    return (
      <Center p="40px">
        <Text fontSize="xl" fontWeight="medium">
          Нет информации о постерах для этого фильма
        </Text>
      </Center>
    );
  }

  return (
    <Box>
      <SimpleGrid columns={{ base: 1, md: 3 }} spacing={5}>
        {posters.docs.map((poster) => (
          <Box key={poster.id} p="5" boxShadow="md" rounded="md">
            <Image src={poster.previewUrl} alt={`Постр для ${movieId}`} />
          </Box>
        ))}
      </SimpleGrid>
      {posters.pages > 1 && (
        <Pagination page={page} maxPage={posters.pages} setPage={setPage} />
      )}
    </Box>
  );
};

export default PosterList;

```

```features/ui/MovieList/MovieList.tsx
import FilmCard from "src/entities/ui/MovieCard/MovieCard";
import { VStack } from "@chakra-ui/react";
import { MovieListProps } from "src/features/models/IMovieList";

const FilmList = ({ movieList }: MovieListProps) => {
  return (
    <VStack gap="3">
      {movieList.map((movie) => (
        <FilmCard key={movie.id} movie={movie} />
      ))}
    </VStack>
  );
};

export default FilmList;

```

```features/ui/MovieReview/MovieReview.tsx
import { Box, Divider, Heading, Tag, Text, VStack } from "@chakra-ui/react";
import { useUnit } from "effector-react";
import React, { useEffect, useState } from "react";
import { Pagination } from "src/entities/ui";
import { getReviewsFx } from "../../api/review";
import { MovieReviewsProps } from "../../models/review";
import { $reviewsStore } from "../../store/review";

const MovieReviews = ({ movieId }: MovieReviewsProps) => {
	const { docs, total, pages } = useUnit($reviewsStore);
	const [currentPage, setCurrentPage] = useState(1);

	useEffect(() => {
		getReviewsFx({
			page: currentPage,
			limit: 5,
			movieId: [movieId.toString()],
		});
	}, [currentPage, movieId]);

	if (total === 0) {
		return <Heading>Отзывов пока нет</Heading>;
	}

	return (
		<Box>
			<Heading as="h3" size="lg" mb={4} w="100%">
				Отзывы
			</Heading>
			{docs.length > 0 ? (
				<VStack divider={<Divider />} spacing={4} w="100%">
					{docs.map((review) => (
						<Box
							key={review.id}
							p={5}
							shadow="md"
							borderWidth="1px"
							borderRadius="md"
							display="flex"
							flexDirection="column"
							gap={4}
							w="100%"
						>
							<Heading as="h4" size="md">
								{review.title || "Без названия"}
							</Heading>
							<Text mt={4}>{review.review}</Text>
							<Text fontSize="sm">
								<Tag>Автор:</Tag>{" "}
								{review.author || "Неизвестен"}
							</Text>
							<Text fontSize="sm">
								<Tag>Оценка пользователя:</Tag>{" "}
								{review.userRating || "Не указана"}
							</Text>
							<Text fontSize="xs" color="gray.500">
								Дата отзыва:{" "}
								{review.createdAt
									? new Date(
											review.createdAt,
										).toLocaleDateString()
									: "-"}
							</Text>
						</Box>
					))}
				</VStack>
			) : (
				<Text>Отзывы отсутствуют.</Text>
			)}
			{pages > 1 && (
				<Pagination
					page={currentPage}
					maxPage={pages}
					setPage={setCurrentPage}
				/>
			)}
		</Box>
	);
};

export default MovieReviews;

```

```features/ui/MovieDetails/MovieDetails.tsx
import {
	Card,
	Heading,
	HStack,
	Image,
	VStack,
	Text,
	Box,
	Center,
	Flex,
	Tag,
	Divider,
} from "@chakra-ui/react";
import { ViewOffIcon } from "@chakra-ui/icons";
import { useEffect } from "react";
import { MovieDetailsProps } from "../../models/IMovieDetails";
import { CircleRating } from "src/shared/ui";
import { useUnit } from "effector-react";
import { $movieDetailsStore } from "src/features/store/MovieDetails";
import { getMovieDetailsFx } from "src/features/api/MovieDetails";
import { PersonList, SimilarMovies } from "src/entities/ui";

const MovieDetails = ({ movieId }: MovieDetailsProps) => {
	const movieDetails = useUnit($movieDetailsStore);

	useEffect(() => {
		getMovieDetailsFx(movieId);
	}, [movieId]);

	return (
		<Card w="100%" p="5" borderRadius="25" gap="25px">
			<Flex wrap="wrap" mb="3">
				<Heading size="xl">{movieDetails.name}</Heading>
				<Tag>+{movieDetails.ageRating}</Tag>
			</Flex>
			<Flex
				direction={{ base: "column", md: "row" }}
				align="center"
				mb="3"
			>
				<Box flexShrink={0}>
					{movieDetails.poster.previewUrl ? (
						<Image
							h="350"
							src={movieDetails.poster.previewUrl}
							alt={`Постер ${movieDetails.name}`}
							borderRadius="20"
						/>
					) : (
						<Card h="250px" w="100%" background="">
							<Center h="100%" w="100%">
								<VStack>
									<ViewOffIcon />
									<Text>Постер отсутствует</Text>
								</VStack>
							</Center>
						</Card>
					)}
				</Box>

				<Box flex="1" p="4">
					<VStack align="left" h="100%" justify="space-between">
						<Flex wrap="wrap" justifyContent="space-evenly">
							<CircleRating rating={movieDetails.rating.kp}>
								Кинопоиск
							</CircleRating>
							<CircleRating rating={movieDetails.rating.imdb}>
								IMDB
							</CircleRating>
							<CircleRating
								rating={movieDetails.rating.filmCritics}
							>
								Кинокритики
							</CircleRating>
							<CircleRating
								rating={movieDetails.rating.filmCritics}
							>
								Рус. критики
							</CircleRating>
						</Flex>
						<Divider />
						<HStack>
							<Tag>Год выхода:</Tag>
							<Text>
								{movieDetails.year || "Год выхода отсутствует"}
							</Text>
						</HStack>
						<Divider />
						<HStack>
							<Tag>Страна:</Tag>
							<Text>
								{movieDetails.countries
									.map((country) => country.name)
									.join(", ") || "Страны отсутствуют"}
							</Text>
						</HStack>
						<Divider />
						<Text>
							<Tag>Описание:</Tag>{" "}
							{movieDetails.description || "Описание отсутствует"}
						</Text>
					</VStack>
				</Box>
			</Flex>
			<PersonList persons={movieDetails.persons} />
			<SimilarMovies movies={movieDetails.similarMovies} />
		</Card>
	);
};

export default MovieDetails;

```

```app/router/AppRouter.tsx
import { MoviePage, LandingPage, NotFoundPage } from "src/pages";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { PATHS } from "./paths";
import { Header } from "src/widgets/ui";

const AppRouter = () => {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path={PATHS.HOME} element={<LandingPage />} />
        <Route path={PATHS.FILM + "/:movieId"} element={<MoviePage />} />

        <Route path={PATHS.NOTFOUND} element={<NotFoundPage />} />
        <Route path="*" element={<Navigate to={PATHS.NOTFOUND} />} />
      </Routes>
    </BrowserRouter>
  );
};

export default AppRouter;

```

```app/router/index.ts
import AppRouter from "./AppRouter";

export default AppRouter;

```

```app/router/paths.ts
export enum PATHS {
  HOME = "/",
  FILM = "/movie",
  NOTFOUND = "/404",
}

```

